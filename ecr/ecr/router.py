def route_ecr(category):
    mapping = {
        "safety-critical": "Flight Safety Engineering Team",
        "avionics": "Avionics Systems Team",
        "documentation": "Compliance Documentation Team",
        "general": "General Engineering Intake"
    }
    return mapping.get(category, "General Engineering Intake")
