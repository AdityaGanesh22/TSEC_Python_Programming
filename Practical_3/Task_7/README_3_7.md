# Practical 3 – Task 7: Prime Number Analyzer

## Objective
Using a function, write a Python program to analyze whether the input number is prime or not.

## Instructions
- Implement the function `is_prime(n)` in `student_code_3_7.py`.
- The function should return True if n is prime, False otherwise.

## Examples
```python
is_prime(7)
# Output: True

is_prime(10)
# Output: False

is_prime(2)
# Output: True

is_prime(1)
# Output: False
```
## Transition from C to Python
In C, you might write:
```c
int isPrime(int n) {
    if (n <= 1) return 0;
    for (int i = 2; i*i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}
```

## How to check your solution
1. Open CLI and navigate to the assignment folder.
2. Run Python and import your function:
   `from student_code_3_7 import *`
3. Call `is_prime(n)` with different values.

## How to Run Autograder
1. Save your solution in `student_code_3_7.py`.
2. Run:
   `python autograder_3_7.py`
   or
   `python3 autograder_3_7.py`
3. Check your score, feedback, and token.

## Notes
- Use a function definition.
- Do not change file or function names.
- Submit your token and screenshot in the Excel sheet.