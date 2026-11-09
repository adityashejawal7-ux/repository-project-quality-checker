# Check-to-Reference Mapping

This document explains what each repository check verifies.

| Check | Purpose |
|---|---|
| README.md | Checks whether project information is available. |
| LICENSE | Checks whether a license file exists. |
| requirements.txt | Checks whether dependencies are documented. |
| .gitignore | Checks whether unnecessary files are excluded. |
| src folder | Checks whether source code folder exists. |
| tests folder | Checks whether testing folder exists. |
| docs folder | Checks whether documentation folder exists. |

## Result Meaning

- PASS: Required item is present.
- MISSING: Required item is not present.

## Safety

The checker only reads the target repository.
It does not modify or delete repository files.