# Practical 5 – Task 3: Logging for Debugging

## Objective
Enhance a Python program by adding logging statements to record the flow of execution and error messages. Use the logging module to configure different logging levels `(INFO, DEBUG, ERROR)`.

## Instructions
- Implement `divide_numbers(a, b)` in `student_code_5_3.py`.
- Configure logging with a format that includes timestamp, level, and message.
- The function should:
  - Log when it starts execution (INFO).
  - Log successful division with details (DEBUG).
  - Log division by zero errors (ERROR).

## Example
Input:
`divide_numbers(10, 2)`

Output:
```
Result: 5.0
Log:
2026-02-09 15:30:00 - INFO - Starting division function
2026-02-09 15:30:00 - DEBUG - Division successful: 10 / 2 = 5.0
```

Input:
`divide_numbers(10, 0)`

Output:
```
Error: Division by zero is not allowed.
Log:
2026-02-09 15:31:00 - INFO - Starting division function
2026-02-09 15:31:00 - ERROR - Attempted division by zero
```

## Transition from C to Python
In C, debugging often relies on printf statements.  
In Python, the logging module provides structured, configurable output with levels.

## How to check your solution
1. Save your solution in `student_code_5_3.py`.
2. Run `autograder_5_3.py`.
3. Check your score, feedback, and Token.

## Notes
- Do not change the function name `divide_numbers()`.
- Use logging levels appropriately.
- Submit your token and screenshot in the Excel sheet.