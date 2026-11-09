import os
import json
import argparse
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "requirements.txt",
    ".gitignore"
]

REQUIRED_FOLDERS = [
    "src",
    "tests",
    "docs"
]


def check_repository(repo_path):

    results = []

    for item in REQUIRED_FILES:
        path = os.path.join(repo_path, item)

        results.append({
            "item": item,
            "type": "File",
            "status": "PASS" if os.path.isfile(path) else "MISSING"
        })

    for item in REQUIRED_FOLDERS:
        path = os.path.join(repo_path, item)

        results.append({
            "item": item,
            "type": "Folder",
            "status": "PASS" if os.path.isdir(path) else "MISSING"
        })

    return results


def main():

    parser = argparse.ArgumentParser(
        description="Read-only Repository Quality Checker"
    )

    parser.add_argument(
        "repository",
        nargs="?",
        default=BASE_DIR,
        help="Path of repository to check"
    )

    args = parser.parse_args()

    repo_path = os.path.abspath(args.repository)

    if not os.path.isdir(repo_path):
        print("Error: Repository path does not exist.")
        return

    results = check_repository(repo_path)

    for result in results:
        print(result["item"], "-", result["status"])

    report = {
        "project": "Repository Project-Quality Checker",
        "repository": repo_path,
        "date": datetime.now().isoformat(),
        "results": results
    }

    report_path = os.path.join(
        BASE_DIR, "reports", "sample_report.json"
    )

    os.makedirs(os.path.dirname(report_path), exist_ok=True)

    with open(report_path, "w") as file:
        json.dump(report, file, indent=4)

    print("\nReport generated successfully!")


if __name__ == "__main__":
    main()