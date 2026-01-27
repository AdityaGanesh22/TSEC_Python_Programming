# Practical 3 – Task 8: Simple Calculator Using Functions

## Objective
Implement a simple Python calculator that takes user input and performs basic arithmetic operations (addition, subtraction, multiplication, division) using functions.

## Instructions
- Implement four functions in student_code_3_8.py:
  - `add(a, b)`
  - `subtract(a, b)`
  - `multiply(a, b)`
  - `divide(a, b)`
- Each function should return the result of the operation.
- Division must raise an error if b == 0.

## Examples
```python
add(5, 3)
# Output: 8

subtract(10, 4)
# Output: 6

multiply(7, 6)
# Output: 42

divide(20, 5)
# Output: 4.0

divide(10, 0)
# Output: ValueError ("Division by zero is not allowed")
```

## Transition from C to Python
In C, you might write separate functions for each operation:
```c
int add(int a, int b) { return a + b; }
int subtract(int a, int b) { return a - b; }
...
```


## How to check your solution
1. Open CLI and navigate to the assignment folder.
2. Run Python and import your functions:
   `from student_code_3_8 import *`
3. Call `add()`, `subtract()`, `multiply()`, `divide()` with different values.

## How to Run Autograder
1. Save your solution in `student_code_3_8.py`.
2. Run:
   `python autograder_3_8.py`
   or
   `python3 autograder_3_8.py`
3. Check your score, feedback, and token.

## Notes
- Use functions for modularity.
- Do not change file or function names.
- Submit your token and screenshot in the Excel sheet.