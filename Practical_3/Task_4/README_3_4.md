# Practical 3 – Task 4: Multiplication Table Generator

## Objective
Write a Python program to take a numerical input from the user and generate its multiplication table using loops.

## Instructions
- Implement the function `generate_table(n, upto=10)` in `student_code_3_4.py`.
- The function should print the multiplication table of n up to 'upto'.
- Default value of 'upto' is 10.

## Examples
```python
generate_table(5)
# Output:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

generate_table(7, 3)
# Output:
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
```

## Transition from C to Python
In C, you might write:
```c
for (int i = 1; i <= 10; i++) {
    printf("%d x %d = %d\n", n, i, n*i);
}
```

## How to check your solution
1. Open CLI and navigate to the assignment folder.
2. Run Python and import your function:
   `from student_code_3_4 import *`
3. Call `generate_table(n)` with different values of n.

## How to Run Autograder
1. Save your solution in `student_code_3_4.py`.
2. Run:
   `python autograder_3_4.py`
   or
   `python3 autograder_3_4.py`
3. Check your score, feedback, and Token.

## Notes
- Use loops to generate the table.
- Do not change file or function names.
- Submit your Token and screenshot in the Excel sheet/Google Form.