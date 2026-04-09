from ecr.classifier import classify_ecr
from ecr.router import route_ecr
from ecr.compliance import generate_checklist
from github.issue_creator import create_issue

def process_ecr(ecr_text):
    category = classify_ecr(ecr_text)
    team = route_ecr(category)
    checklist = generate_checklist(category)

    issue = create_issue(
        title=f"[{category.upper()}] New Engineering Change Request",
        body=f"""
        ### ECR
        {ecr_text}

        ### Category
        {category}

        ### Assigned Team
        {team}

        ### Compliance Checklist
        {checklist}
        """
    )

    return issue

if __name__ == "__main__":
    sample = "Update hydraulic system redundancy logic for 737 subsystem controller"
    print(process_ecr(sample))
