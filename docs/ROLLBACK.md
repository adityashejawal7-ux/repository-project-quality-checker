# Rollback Notes

## Purpose
This project is a read-only repository checker.

## Changes Made
- Checks required files and folders.
- Generates a JSON report.
- Does not modify target repository files.

## Rollback Procedure
1. Stop the checker if it is running.
2. Delete the generated report from the reports folder if it is no longer needed.
3. Remove the project folder if you want to uninstall the checker.

## Safety
The checker does not delete, edit, or overwrite files in the target repository.