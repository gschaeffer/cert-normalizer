import json

from ..sample_data import sample_data


def test_endpoints(client):
    payload = {"job_id": 1212, "raw_content": sample_data[12]}
    keys = [
        "expire_date",
        "issue_date",
        "issue_re_date",
        "issued_to_email",
        "issued_to_name",
        "job_id",
        "number",
        "raw_content",
        "title",
        "vendor",
    ]

    # test post with known job_id
    response = client.post(
        "/",
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert type(data) is dict
    assert data["response"]["job_id"] == 1212
    assert data["response"]["vendor"] == "cncf"
    assert data["response"]["issued_to_name"] == "Steve Rooker"
    assert data["response"]["number"] == "LF-iya9vve8wo"
    assert data["response"]["issue_date"] == "2022-05-10"
    assert data["response"]["issue_re_date"] == "2022-05-10"
    assert data["response"]["expire_date"] == "2024-05-10"
    assert data["response"]["title"] == "certified kubernetes security"

    # ensure all keys are in response structure
    assert "response" in data.keys()
    for k in keys:
        assert k in data["response"].keys()

    # test post with unknown job_id
    payload = {"raw_content": sample_data[0]}
    response = client.post(
        "/",
        data=json.dumps(payload),
        headers={"Content-Type": "application/json"},
    )
    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data["response"]["job_id"]) > 10

    # test get on nornalize for handled error response
    response = client.get("/")
    assert response.status_code == 200
