# Practical 5 – Task 5: Scientific Debugging Techniques

## Objective
Provide a Python program with multiple logic and runtime errors. Instruct students to apply scientific debugging techniques, such as binary search debugging, to identify and resolve the issues methodically.

## Instructions
- Open `student_code_5_5.py`.
- The function `buggy_program()` contains intentional errors:
  1. Variable used before assignment.
  2. Division by zero.
  3. Loop going out of range.
  4. Invalid type operation (string + integer).
- Run the program and observe the errors.
- Apply scientific debugging techniques:
  - Isolate the problem area.
  - Use print statements or logging to instrument the code.
  - Hypothesize the cause of the error.
  - Test fixes step by step.
  - Iterate until the program runs correctly.

## Example Debugging Approach
- Start by commenting out sections of code to isolate where the error occurs.
- Use binary search debugging: disable half the code, run the program, then narrow down.
- Add print statements to check variable values before operations.
- Correct each error methodically.

## Transition from C to Python
In C, debugging often requires gdb or IDE tools.  
In Python, you can use pdb, IDE debuggers, or scientific debugging techniques with print/logging.

## How to check your solution
- Run `autograder_5_5.py`.
- The autograder verifies that buggy_program exists.
- Debugging must be demonstrated manually in class.

## Notes
- Do not remove `buggy_program`; it is required for demonstration.
- Submit your token and screenshot in the Excel sheet.