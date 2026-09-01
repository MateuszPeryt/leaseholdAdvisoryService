"""Small, explainable rules for the prototype. This is not legal advice."""

CATEGORIES = {
    "service_charges": {
        "title": "Service charges and bills",
        "summary": "You appear to have a question about a bill, service charge, or major works cost.",
        "steps": [
            "Keep the bill and any letters in a safe place.",
            "Check what the charge is for and when payment is due.",
            "Ask the landlord or managing agent for a clear breakdown if you need one.",
        ],
    },
    "repairs": {
        "title": "Repairs, maintenance, or building safety",
        "summary": "You appear to have a question about repair work, maintenance, or building safety.",
        "steps": [
            "Write down what is wrong and when you first noticed it.",
            "Tell the landlord or managing agent in writing and keep a copy.",
            "If there is an immediate danger, contact the emergency services first.",
        ],
    },
    "lease_changes": {
        "title": "Buying, selling, or extending a lease",
        "summary": "You appear to have a question about changing, buying, selling, or extending a lease.",
        "steps": [
            "Check your lease for important dates and terms.",
            "Collect any letters or documents about the sale, purchase, or extension.",
            "Get specialist advice before agreeing to a major legal or financial step.",
        ],
    },
    "management_issue": {
        "title": "A problem with a landlord, freeholder, or managing agent",
        "summary": "You appear to have a problem with the person or company managing your home.",
        "steps": [
            "Keep a dated record of what happened and any messages you sent or received.",
            "Use the landlord's or managing agent's complaints process if they have one.",
            "Ask for help if you are unsure which organisation is responsible.",
        ],
    },
    "not_sure": {
        "title": "We are not sure which topic fits",
        "summary": "Your question may need a closer look. We can still help you find the right place to start.",
        "steps": [
            "Write down the main problem and any important dates.",
            "Keep copies of letters, bills, and emails about the issue.",
            "Contact the Leasehold Advisory Service for general guidance.",
        ],
    },
}

SCENARIO_TO_CATEGORY = {
    "service-charge": "service_charges",
    "repair": "repairs",
    "lease-change": "lease_changes",
    "management": "management_issue",
}

KEYWORDS = {
    "service_charges": ("service charge", "major works", "invoice", "bill", "demand"),
    "repairs": ("repair", "damp", "leak", "mould", "cladding", "fire safety"),
    "lease_changes": ("extend", "extension", "lease length", "sell", "selling", "buy", "purchase"),
    "management_issue": ("managing agent", "freeholder", "landlord", "complaint"),
}


def classify(scenario: str, description: str) -> dict:
    """Return a category. A selected scenario always takes priority."""
    if scenario in SCENARIO_TO_CATEGORY:
        return build_result(SCENARIO_TO_CATEGORY[scenario], "your selected situation")

    text = description.lower()
    scores = {
        category: sum(keyword in text for keyword in keywords)
        for category, keywords in KEYWORDS.items()
    }
    highest_score = max(scores.values(), default=0)
    matches = [category for category, score in scores.items() if score == highest_score and score > 0]

    if len(matches) != 1:
        return build_result("not_sure", "the information provided")

    return build_result(matches[0], "words in your description")


def build_result(category: str, matched_by: str) -> dict:
    return {"category": category, "matchedBy": matched_by, **CATEGORIES[category]}

