from normalizer import normalizer
import json

"""initialization

    n = normalizer.Normalizer(
        job_id=job_nbr,
        raw_content=raw_content,
        members=app.config.get("MEMBERS", []),
    )
"""

data = {
    "job_id": "adasdadasd",
    "raw_content": "Google Cloud This acknowledges that Jules Masterson has successfully completed all the requirements to be recognized as Series ID: 57896 Issue Date: 25 Feb 2022 Expiration Date: 25 Feb 2024 Certification ID: VAAloa Certified As: Jules Masterson Google Cloud Certified Professional Cloud Architect The non time Thomas Kurian CEO, Google Cloud GOOGLE Cloud Architect CLOUD CERTIFIED PROFESSIONAL",
    "members": ["Jules Masterson"],
}
n = normalizer.Normalizer(**data)
print(json.dumps(n.data, indent=2))
