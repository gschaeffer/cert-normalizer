import json
import logging
import uuid

import spacy
from spacy.matcher import Matcher, PhraseMatcher


class NormalizerBase:
    def __init__(self, **kwargs):
        """create standard key-value structure for all responses.
        non-discoverable values: issued_to_email, number (?)
        NLP:
            - get dates and sort
            - get vendor organization
            - get title
            - get issued_to_name
            - get number
        """

        self._kwargs = kwargs
        self._vals = {
            "expire_date": "",
            "issue_date": "",
            "issue_re_date": "",
            "issued_to_email": "",
            "issued_to_name": "",
            "job_id": "",
            "number": "",
            "raw_content": "",
            "title": "",
            "vendor": "",
        }

        self._vals.update(kwargs)
        if "members" in self._vals:
            self._vals.pop("members")

        if self.job_id == "":
            self.job_id = uuid.uuid4().hex

        self.set_vendor()
        self.set_name()
        self.set_number()
        self.set_title()
        self.set_dates()

    def get(self, arg):
        if arg in self._vals:
            return self._vals[arg]

    @property
    def data(self):
        return self._vals

    @property
    def as_json(self):
        return json.dumps(self._vals, indent=4)

    def __str__(self):
        return self._vals

    """ 
    attribute property getter/setters
    --------------------------------------------------------------------------------"""

    @property
    def job_id(self):
        return self.get("job_id")

    @job_id.setter
    def job_id(self, val):
        self._vals["job_id"] = val

    @property
    def expire_date(self):
        return self.get("expire_date")

    @expire_date.setter
    def expire_date(self, val):
        self._vals["expire_date"] = val

    @property
    def issue_date(self):
        return self.get("issue_date")

    @issue_date.setter
    def issue_date(self, val):
        self._vals["issue_date"] = val

    @property
    def issue_re_date(self):
        return self.get("issue_re_date")

    @issue_re_date.setter
    def issue_re_date(self, val):
        self._vals["issue_re_date"] = val

    @property
    def issued_to_name(self):
        return self.get("issued_to_name")

    @issued_to_name.setter
    def issued_to_name(self, val):
        self._vals["issued_to_name"] = val

    @property
    def number(self):
        return self.get("number")

    @number.setter
    def number(self, val):
        self._vals["number"] = val

    @property
    def title(self):
        return self.get("title")

    @title.setter
    def title(self, val):
        self._vals["title"] = val

    @property
    def raw_content(self):
        return self.get("raw_content")

    @raw_content.setter
    def raw_content(self, val):
        self._vals["raw_content"] = val

    @property
    def vendor(self):
        return self.get("vendor")

    @vendor.setter
    def vendor(self, val):
        self._vals["vendor"] = val

    """
    functions
    --------------------------------------------------------------------------------"""

    def set_vendor(self):
        vendors = [
            "aws",
            "cncf",
            "cloud native comput",
            "doit",
            "google",
            "hashicorp",
            "microsoft",
            "snowflake",
            "tetrate",
        ]

        for v in vendors:
            if v in self.raw_content.lower():
                if "native" in v:
                    v = "cncf"
                self.vendor = v
                return
        self.vendor = "other"

    def set_name(self):
        """names list must come from database extracts."""

        names = []
        if "members" in self._kwargs:
            names = self._kwargs["members"]

        nlp = spacy.blank("en")
        matcher = PhraseMatcher(nlp.vocab, attr="LOWER")  # case insensitive matching.

        patterns = [nlp.make_doc(text) for text in names]
        matcher.add("issue_to", patterns)

        doc = nlp(self.raw_content)
        matches = matcher(doc)
        for match_id, start, end in matches:
            self.issued_to_name += doc[start:end].text
            return  # only need the first occurrence of the name

    def set_number(self):
        from .number_patterns import number_patterns

        nlp = spacy.blank("en")
        doc = nlp(self.raw_content)
        matcher = Matcher(nlp.vocab)

        matcher.add("certificate_number", number_patterns)
        matches = matcher(doc)
        if self.vendor == "google":
            # Google is a combination of series and certification IDs
            vals = []
            for match_id, start, end in matches:
                vals.append(doc[start:end].text)
            vals.sort(reverse=True)  # Series before Certification
            parts = []
            for i in vals:
                parts.append(i.split(" ")[-1])
            self.number = "-".join(parts)
        else:
            for match_id, start, end in matches:
                self.number = doc[start:end].text.split(" ")[-1]

    def set_title(self):
        from .title_patterns import (
            aws_title_patterns,
            azr_title_patterns,
            cncf_title_patterns,
            doit_title_patterns,
            gcp_title_patterns,
            hashicorp_title_patterns,
            tetrate_title_patterns,
            unknown_title_patterns,
        )

        nlp = spacy.blank("en")
        matcher = PhraseMatcher(nlp.vocab)

        if self.vendor == "aws":
            patterns = [nlp.make_doc(text) for text in aws_title_patterns]
        elif self.vendor == "cncf":
            patterns = [nlp.make_doc(text) for text in cncf_title_patterns]
        elif self.vendor == "doit":
            patterns = [nlp.make_doc(text) for text in doit_title_patterns]
        elif self.vendor == "google":
            patterns = [nlp.make_doc(text) for text in gcp_title_patterns]
        elif self.vendor == "hashicorp":
            patterns = [nlp.make_doc(text) for text in hashicorp_title_patterns]
        elif self.vendor == "microsoft":
            patterns = [nlp.make_doc(text) for text in azr_title_patterns]
        elif self.vendor == "tetrate":
            patterns = [nlp.make_doc(text) for text in tetrate_title_patterns]
        else:
            patterns = [nlp.make_doc(text) for text in unknown_title_patterns]

        matcher.add("titles", patterns)

        doc = nlp(self.raw_content.lower())
        matches = matcher(doc)

        for match_id, start, end in matches:
            self.title = doc[start:end].text

    def set_dates(self):
        from .date_patterns import common_date_formats, common_date_patterns

        nlp = spacy.blank("en")
        doc = nlp(self.raw_content)
        matcher = Matcher(nlp.vocab)
        matcher.add("date_patterns", common_date_patterns)

        matches = matcher(doc)
        dates = []
        from . import date_utils

        for match_id, start, end in matches:
            val = doc[start:end].text
            val = date_utils._iso_format(val, common_date_formats)
            if val is not None:
                dates.append(val)
        dates.sort()
        if len(dates) > 0:  # issue date
            self.issue_date = dates[0]
        if len(dates) > 1:  # expire date
            self.expire_date = dates[-1]
        # if issue date is  within 2 years, set as latest date
        self.issue_re_date = date_utils.get_issue_re_date(self.issue_date, self.vendor)
        if len(self.expire_date) != 10:
            self.expire_date = date_utils.get_expire_date(
                self.issue_date, self.expire_date, self.vendor, self.title
            )
