def classify_ecr(text):
    text = text.lower()

    if "hydraulic" in text or "structural" in text:
        return "safety-critical"
    if "software" in text or "controller" in text:
        return "avionics"
    if "documentation" in text:
        return "documentation"
    return "general"
