""" 
spacy NLP patterns for date values identification.

Notes: Date patterns encountered:

- AZR patterns
    Date of achievement: December 16, 2022
    Valid until: December 16, 2022
- AWS
    Issue Date: 18 Mar 2022 - Expiration Date: 18 Mar 2023
    Issue Date May 19, 2020 - Expiration Date May 19, 2023
    Issue Date: Nov 26, 2020 - Expiration Date: Nov 26, 2023
- CNCF
    December 23, 2022
- GCP
    Issue Date: 25 Feb 2022 - Expiration Date: 25 Feb 2024
- Hashi
    2022-08-31
- Snowflake & Tetrate
    December 23, 2022

Common patterns: 
    --- AZR, AWS, CNCF, Hashi, Snow, Tetrate
    2022-08-31
    December 23, 2022
    Nov 19, 2023
    --- AWS, GCP
    18 Mar 2023
"""

common_date_formats = ["YYYY-M-D", "MMMM D, YYYY", "MMM D, YYYY", "D MMM YYYY"]

common_date_patterns = [
    [  # 2022-08-31: Hashicorp
        {"IS_DIGIT": True},
        {"TEXT": "-"},
        {"IS_DIGIT": True},
        {"TEXT": "-"},
        {"IS_DIGIT": True},
    ],
    [  # December 23, 2022 OR Dec 23, 2022: AZR, CNCF, Snow, Tetrate
        {"IS_ALPHA": True},
        {"IS_DIGIT": True},
        {"TEXT": ","},
        {"IS_DIGIT": True},
    ],
    [  # 23 Dec 2022: AWS, GCP
        {"IS_DIGIT": True},
        {"IS_ALPHA": True},
        {"IS_DIGIT": True},
    ],
]
