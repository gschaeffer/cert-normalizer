import arrow


def _iso_format(val, date_patterns):
    """loop known patterns. End (return) when match (date) is found."""
    for p in date_patterns:
        try:
            # arrow.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss')
            a = arrow.get(val, p)
            # print(f"date format match found for '{val}' to pattern: {p}")
            return f"{a.year}-{str(a.month).zfill(2)}-{str(a.day).zfill(2)}"
        except Exception as ex:
            pass


def get_issue_re_date(issue_date_iso, vendor):
    try:
        duration = 2
        # AWS: 3
        # CNCF: CKA/CKAD=3, CKS=2
        # Google: 2
        # Hashi: 2
        # Azure: 2
        if "aws" in vendor:
            duration = 3

        a = arrow.get(issue_date_iso)
        # if issue_date is within 2 years of now, set re_date to issue_date
        if a.shift(years=+duration) > arrow.utcnow():
            return issue_date_iso
        return ""
    except Exception as ex:
        return ""


def get_expire_date(issue_date_iso, expire_date_iso, vendor, title):
    try:
        duration = 2
        # AWS: 3
        # CNCF: CKA/CKAD=3, CKS=2
        # Google: 2
        # Hashi: 2
        # Azure: 2
        if "aws" in vendor:
            duration = 3
        if "cncf" in vendor and "security" not in title:
            duration = 3

        if vendor in ["aws", "microsoft", "cncf", "google", "hashicorp"]:
            a = arrow.get(issue_date_iso).shift(years=+duration)
            return f"{a.year}-{str(a.month).zfill(2)}-{str(a.day).zfill(2)}"
        return ""
    except Exception as ex:
        return ""
