# Repository Project-Quality Checker

## 1. Project Overview
The Repository Project-Quality Checker is a Python-based tool that checks the quality and structure of a software project repository.

It identifies missing required files and folders and generates a JSON report.

## 2. Objectives
- Check required project files.
- Verify folder structure.
- Identify missing elements.
- Generate an automatic JSON report.
- Perform checks without modifying repository files.

## 3. Technologies Used
- Python
- Visual Studio Code
- JSON
- Git and GitHub

## 4. Project Features
- Required file checking.
- Required folder checking.
- PASS and MISSING status.
- Automatic JSON report generation.
- Read-only repository inspection.

## 5. Project Structure

```text
Repository-Project-Quality-Checker/
├── src/
│   └── checker.py
├── tests/
├── reports/
│   └── sample_report.json
├── docs/
├── evidence/
└── README.md
```

## 6. Installation

1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python src/checker.py
```

## 7. Output

The checker displays PASS or MISSING status for required files and folders.

It also generates a JSON report inside the reports folder.

## 8. Limitations

- Currently checks predefined files and folders.
- Does not automatically repair missing files.
- Does not modify repository content.

## 9. Future Improvements

- Add more repository checks.
- Improve report generation.
- Add automated testing.
- Support additional project standards.

## 10. Author
Task 2 Assignment Project