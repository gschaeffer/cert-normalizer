""" 
spacy NLP patterns for name (issued to) identification.

"""
common_issue_to_formats = ["YYYY-M-D", "MMMM D, YYYY", "MMM D, YYYY", "D MMM YYYY"]

common_issue_to_patterns = [
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
