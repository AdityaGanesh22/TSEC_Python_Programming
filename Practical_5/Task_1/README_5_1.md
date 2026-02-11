# Practical 5 – Task 1: Basic Exception Handling

## Objective
Write a Python program that takes two numbers as input and performs division.
Implement exception handling to manage division by zero and invalid input errors gracefully.

## Instructions
- Implement `divide_numbers()` in `student_code_5_1.py`.
- The function should:
  - Ask the user for two numbers.
  - Perform division.
  - Handle ZeroDivisionError with a clear message.
  - Handle ValueError for invalid inputs with a clear message.

## Example
Input:
```
Enter first number: 10
Enter second number: 2
```

Output:
```
Result: 5.0
```

Input:
```
Enter first number: 10
Enter second number: 0
```

Output:
`Error: Division by zero is not allowed.`

Input:
```
Enter first number: abc
Enter second number: 2
```

Output:
`Error: Invalid input. Please enter numeric values.`

## Transition from C to Python
In C, you would use scanf for input and check conditions manually.
In Python, exceptions simplify error handling with try/except blocks.

## How to check your solution
1. Save your solution in `student_code_5_1.py`.
2. Run `autograder_5_1.py`.
3. Check your score, feedback, and token.

## Notes
- Do not change the function name `divide_numbers()`.
- Handle exceptions gracefully.
- Submit your token and screenshot in the Excel sheet.