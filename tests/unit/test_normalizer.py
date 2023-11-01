from app.modules.normalizer import Normalizer

from ..sample_data import sample_data


def test_normalizer():
    """
    GIVEN a Normalizer object
    WHEN the property is set
    THEN check the response is correct
    """
    content = sample_data[0]
    n = Normalizer(raw_content=content)
    assert n.vendor == "google"
    assert n.number == "57896-VAAloa"
    assert n.issue_date == "2022-02-25"
    assert n.issue_re_date == "2022-02-25"
    assert n.expire_date == "2024-02-25"
    assert n.title == "professional cloud architect"

    content = sample_data[4]
    n = Normalizer(raw_content=content)
    assert n.vendor == "aws"
    assert n.number == "XPHV7GPLP1VQ115J"
    assert n.issue_date == "2020-11-26"
    assert n.issue_re_date == "2020-11-26"
    assert n.expire_date == "2023-11-26"
    assert n.title == "cloud practitioner"

    # confirm re_date unknown.
    content = sample_data[5]
    n = Normalizer(raw_content=content)
    assert n.expire_date == "2022-05-19"
    assert n.issue_date == "2019-05-19"
    assert n.issue_re_date == ""

    assert n.number == "YZ3HPS72ENBQQCS5"
    assert n.title == "solutions architect - professional"
    assert n.vendor == "aws"

    content = sample_data[12]  # CNCF, security
    n = Normalizer(raw_content=content)
    assert n.expire_date == "2024-05-10"
    assert n.issue_date == "2022-05-10"
    assert n.issue_re_date == "2022-05-10"

    assert n.number == "LF-iya9vve8wo"
    assert n.title == "certified kubernetes security"
    assert n.vendor == "cncf"

    content = sample_data[13]  # CNCF
    n = Normalizer(raw_content=content)
    assert n.expire_date == "2025-04-25"
    assert n.issue_date == "2022-04-25"
    assert n.issue_re_date == "2022-04-25"

    assert n.number == "LF-z7r9h79xpo"
    assert n.title == "certified kubernetes administrator"
    assert n.vendor == "cncf"

    content = sample_data[14]
    n = Normalizer(raw_content=content)
    assert n.expire_date == "2024-08-31"
    assert n.issue_date == "2022-08-31"
    assert n.issue_re_date == "2022-08-31"

    assert len(n.number) == 0
    assert n.title == "vault associate"
    assert n.vendor == "hashicorp"

    # assert len(app.config["SECRET_KEY"]) > 4

    # assert type(app.config["UPLOAD_EXTENSIONS"]) is list
    # assert len(app.config["UPLOAD_EXTENSIONS"]) >= 0
