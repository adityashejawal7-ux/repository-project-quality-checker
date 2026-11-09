# Technical Report
## Repository Project-Quality Checker

### 1. Introduction
The Repository Project-Quality Checker is a Python-based tool that checks the basic quality of a software repository.

### 2. Objective
The main objective is to identify missing files and folders in a software project.

### 3. Technologies Used
- Python
- Visual Studio Code
- JSON

### 4. Main Features
- Checks README.md.
- Checks LICENSE.
- Checks requirements.txt.
- Checks .gitignore.
- Checks src, tests and docs folders.
- Generates a JSON report.

### 5. Working
The program checks whether required files and folders are present. It displays PASS or MISSING results and generates a JSON report.

### 6. Safety
The tool is designed to inspect repository contents without modifying the target repository.

### 7. Limitations
- Checks only predefined files and folders.
- Does not perform advanced code quality analysis.
- Does not check software vulnerabilities.

### 8. Conclusion
This project helps developers identify missing repository files and maintain basic project organization.