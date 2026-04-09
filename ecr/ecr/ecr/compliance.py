def generate_checklist(category):
    base = [
        "Verify FAA compliance impact",
        "Run regression test suite",
        "Review by senior engineer"
    ]

    if category == "safety-critical":
        base += [
            "Dual engineering sign-off required",
            "Safety impact analysis (SIA)",
            "Hardware-in-the-loop simulation required"
        ]

    return "\n- " + "\n- ".join(base)
