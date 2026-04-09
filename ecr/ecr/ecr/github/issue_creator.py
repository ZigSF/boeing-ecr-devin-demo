def create_issue(title, body):
    # For demo purposes (no real GitHub API required)
    print("\n--- CREATING GITHUB ISSUE ---")
    print("TITLE:", title)
    print(body)
    print("--- END ISSUE ---\n")

    return {
        "status": "created",
        "title": title
    }
