# Input Inventory and Validation

Use this reference during Phase 1 of the candidate-prioritization workflow.

## Objective

Create a validated input manifest before interpreting either role or evaluating any candidate.

## Procedure

Before interpreting either role or evaluating any candidate:

1. Create an inventory of every supplied file.
2. Record each file's name, type, readable status, and probable purpose.
3. Identify exactly two files as job descriptions.
4. Label the two roles consistently as Job A and Job B.
5. Identify the remaining valid files as candidate profiles.
6. Detect unreadable, unsupported, empty, incomplete, or duplicated files.
7. Assign a stable candidate identifier using the candidate's name when available and the source filename as a fallback.
8. Record all excluded files and the reason for exclusion.
9. Confirm that the number of valid candidate profiles matches the number that will be evaluated.

Do not begin scoring or classification during this phase.

## Stop Conditions

Stop and ask the user for clarification when:

- Fewer or more than two job descriptions are present and their intended roles cannot be determined reliably.
- No readable candidate profiles are available.
- Job A and Job B cannot be distinguished clearly.
- Multiple files appear to represent the same candidate and the duplication cannot be resolved safely.

## Required Manifest

The phase is complete only when there is a validated input manifest containing:

- Job A source file.
- Job B source file.
- Every valid candidate profile.
- Every excluded file.
- The exclusion reason for each excluded file.
- The final number of candidates approved for evaluation.