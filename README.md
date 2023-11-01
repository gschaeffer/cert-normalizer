### Purpose

Normalizer service accepts scanned certificate data and attempts to decompose the content into structured values.

The guaranteed result is json with known attributes.

```
{
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
```

### Flow

1. Url request

```
export CERT_DATA=... # raw_content of certificate

export HEADER="Content-type: application/json"
export HEADER='{\"Content-type\": \"application/json\"}'
export URL=http://localhost:8080
"{\"raw_content\": \"Google Cloud This acknowledges that Nikhil Stevens has successfully completed all the requirements to be recognized as a Series ID: 52886 Issue Date: 18 Mar 2022 Expiration Date: 18 Mar 2024 Certification ID: vYTglw Certified As: Nikhil Stevens GOOGLE CLOUD CERTIFIED ASSOCIATE CLOUD ENGINEER The nationa ma Thomas Kurian CEO, Google Cloud Cloud Google Certified ASSOCIATE CLOUD ENGINEER\"}"

"{\"raw_content\": \"NATIVE COMPUTING FOUNDATION LOUD NATIVE ID NATIVE CLOUD NATIVE OUD NATIVE UTING FOUNDATION COMPUTING FOUNDATI NATIVE CLOUD COMPUTING FOUNDATIO CLOUD NATIVE CLO OUD NATIV COMPUTING FOUNDATION \u043e\u043b The Cloud Native Computing Foundation hereby certifies that FOUNDATION CERTIFIED kubernetes COMPUTING FO APPLICATION DEVELOPER \u043a\u0438 NATIVE FOUNDATION Eran Chezroni has successfully completed the program requirements to be recognized as a DAN KOHN, EXECUTIVE DIRECTOR CLOUD NATIVE COMPUTING FOUNDATION Certified Kubernetes Application Developer TING FOUNDATION OUNDATION ATIVE D NATIVE, UD NATIVE PUTING FOUNDATION June 8, 2019 DATE OF COMPLETION TION OMPUTING FO OUD NO COMPUTING FOU OUD NA FOUNDATION MPUTING FOUND CLOUD N COMPUTING UD NATI NATIVE CLOUD NATIVE CKAD-1900-0833-0100 CERTIFICATE ID NUMBER CLOU COMPUT CLOUD NATIV COMPUTING FOUNDATION CLOUD NATIVE CLOC LOUD NATIVE CLOU MPUTING FOUR CLOUD COMPUTIN\"}"


curl -X POST -H $HEADER -d "{\"raw_content\": \"$CERT_DATA\"}" $URL
```

### Installation

- Pipeline should run pytest before deployment.
- TBD

### Integrations

- app-settings-api: 
  - Name recognition requires a valid python list of names. Otherwise, name will be blank.
  - app-settings-api should be set in .env vars.
