# Practical 3 – Task 5: Fibonacci Sequence Generator

## Objective
Develop a Python program to print the Fibonacci sequence using a while loop.

## Instructions
- Implement the function `fibonacci_sequence(limit)` in `student_code_3_5.py`.
- The function should print the Fibonacci sequence up to 'limit' terms.
- Use a while loop, not a for loop.

## Examples
```python
fibonacci_sequence(5)
# Output: 0 1 1 2 3

fibonacci_sequence(7)
# Output: 0 1 1 2 3 5 8
```

## Transition from C to Python
In C, you might write:
```c
int a = 0, b = 1, count = 0;
while (count < limit) {
    printf("%d ", a);
    int temp = a + b;
    a = b;
    b = temp;
    count++;
}
```

## How to check your solution
1. Open CLI and navigate to the assignment folder.
2. Run Python and import your function:
   `from student_code_3_5 import *`
3. Call `fibonacci_sequence(limit)` with different values.

## How to Run Autograder
1. Save your solution in `student_code_3_5.py`.
2. Run:
   `python autograder_3_5.py`
   or
   `python3 autograder_3_5.py`
3. Check your score, feedback, and token.

## Notes
- Use a while loop.
- Do not change file or function names.
- Submit your token and screenshot in the Excel sheet.