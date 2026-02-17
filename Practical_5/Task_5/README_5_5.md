# Practical 5 – Task 5: Scientific Debugging Techniques

## Objective
Provide a Python program with multiple logic and runtime errors. Students must apply scientific debugging techniques, such as binary search debugging, to identify and resolve the issues methodically.

## Instructions
- The provided code implements a binary search algorithm but contains errors.
- Students should not rename the function binary_search.
- Apply debugging techniques to:
  - Trace variable values step by step.
  - Narrow down the location of errors using binary search debugging.
  - Fix logical mistakes and runtime issues.
- The corrected function should return:
  - The index of the target if found.
  - -1 if the target is not found.

## Example Debugging Strategy
1. Insert print statements or use pdb to trace values of `left`, `right`, and `mid`.
2. Check boundary conditions.
3. Verify updates to `left` and `right` pointers.
4. Ensure the return value matches the specification.

## Notes
- Do not remove or rename the function binary_search.
- The autograder will test both cases: target present and target absent.
- Focus on methodical debugging rather than guessing.