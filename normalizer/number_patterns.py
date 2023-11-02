""" 
spacy NLP patterns for certification number identification.

https://spacy.io/usage/rule-based-matching
https://demos.explosion.ai/matcher
"""
number_patterns = [
    [  # AZR
        {"TEXT": "Certification"},
        {"TEXT": "Number"},
        {"TEXT": ":"},
        {"IS_ASCII": True},
        {"TEXT": "-"},
        {"IS_ASCII": True},
    ],
    [  # AWS
        {"TEXT": "Validation"},
        {"TEXT": "Number"},
        {"IS_ASCII": True},
    ],
    [  # AWS
        {"TEXT": "VALIDATION"},
        {"TEXT": "NUMBER"},
        {"TEXT": ":"},
        {"IS_ASCII": True},
    ],
    [  # CNCF: CKA, CKS, CKAD
        {"TEXT": "LF"},
        {"TEXT": "-"},
        {"IS_ASCII": True},
    ],
    [  # CNCF: CKA pattern CKAD-####-####-####
        {"LENGTH": 8, "IS_UPPER": True},
        {"IS_ASCII": True},
        {"IS_DIGIT": True, "LENGTH": 4},
        {"IS_ASCII": True},
        {"IS_DIGIT": True, "LENGTH": 4},
    ],
    [  # CNCF: CKA pattern CKAD-####-######-####
        {"LENGTH": 8, "IS_UPPER": True},
        {"IS_ASCII": True},
        {"IS_DIGIT": True, "LENGTH": 6},
        {"IS_ASCII": True},
        {"IS_DIGIT": True, "LENGTH": 4},
    ],
    [  # CNCF: CKAD pattern CKAD-####-####-####
        {"LENGTH": 9, "IS_UPPER": True},
        {"IS_ASCII": True},
        {"IS_DIGIT": True, "LENGTH": 4},
        {"IS_ASCII": True},
        {"IS_DIGIT": True, "LENGTH": 4},
    ],
    [  # CNCF: CKAD pattern CKAD-####-######-####
        {"LENGTH": 9, "IS_UPPER": True},
        {"IS_ASCII": True},
        {"IS_DIGIT": True, "LENGTH": 6},
        {"IS_ASCII": True},
        {"IS_DIGIT": True, "LENGTH": 4},
    ],
    [  # Google series
        {"TEXT": "Series"},
        {"TEXT": "ID"},
        {"TEXT": ":"},
        {"IS_DIGIT": True},
    ],
    [  # Google number
        {"TEXT": "Certification"},
        {"TEXT": "ID"},
        {"TEXT": ":"},
        {"IS_ASCII": True},
    ],
]
