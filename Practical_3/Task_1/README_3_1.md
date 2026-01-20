# Practical 3 – Task 1: Triangle Pattern Generator Using Loops

## Objective
Write a Python program to print a triangle pattern using loops. This task highlights how loops in Python compare to loops in C.

## Instructions
- Implement the function generate_triangle(n) in `student_code_3_1.py`.
- The function should print a triangle of stars with n rows.
- Example for n=4:
```python
  *
  **
  ***
  ****
  ```

## Transition from C to Python
In C, you might write:
```c
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
        printf("*");
    }
    printf("\n");
}
```

In Python, the same logic is simpler:
```python
for i in range():
    print()
```
## Examples
```python
generate_triangle(3)
# Output:
*
**
***

generate_triangle(5)
# Output:
*
**
***
****
*****
```
## How to check your solution
1. Open CLI and navigate to the assignment folder.
2. Run Python and import your function:
   `from student_code_3_1 import *`
3. Call `generate_triangle(n)` with different values of `n`.

## How to Run Autograder
1. Save your solution in `student_code_3_1.py`.
2. Run:
   `python autograder_3_1.py`
   or
   `python3 autograder_3_1.py`
3. Check your score, feedback, and Token.

## Notes
- Use loops to generate the pattern.
- Compare the syntax differences between C and Python.
- Do not change file or function names.
- Submit your Token and screenshot in the Excel sheet/Google Form.