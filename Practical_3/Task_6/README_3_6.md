# Practical 3 – Task 6: Factorial Generator

## Objective
Design a Python program to compute the factorial of a given integer N.

## Instructions
- Implement the function `factorial(n)` in `student_code_3_6.py`.
- The function should return the factorial of n.
- Factorial is defined as:
  n! = n × (n-1) × (n-2) × ... × 1
- By definition, 0! = 1.

## Examples
```python
factorial(5)
# Output: 120

factorial(0)
# Output: 1

factorial(7)
# Output: 5040
```
## Transition from C to Python
In C, you might write:
```c
int result = 1;
while (n > 0) {
    result *= n;
    n--;
}
printf("%d", result);
```

## How to check your solution
1. Open CLI and navigate to the assignment folder.
2. Run Python and import your function:
   `from student_code_3_6 import *`
3. Call `factorial(n)` with different values.

## How to Run Autograder
1. Save your solution in `student_code_3_6.py`.
2. Run:
   `python autograder_3_6.py`
   or
   `python3 autograder_3_6.py`
3. Check your score, feedback, and token.

## Notes
- Use a while loop or iterative logic.
- Do not change file or function names.
- Submit your token and screenshot in the Excel sheet.