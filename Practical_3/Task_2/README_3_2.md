# Practical 3 – Task 2: Number Type Identifier

## Objective
Develop a Python program that takes a numerical input and identifies whether it is even or odd, using conditional statements and loops.

## Instructions
- Implement the following functions in `student_code_3_2.py`:
  1. `identify_number_type(n)`
     - Returns `"Even"` if n is even, `"Odd"` if n is odd.
  2. `identify_range(start, end)`
     - Uses a loop to check numbers from start to end.
     - Returns a list of strings like `["Odd", "Even", "Odd", ...]`.

## Examples
```python
identify_number_type(4)
# Output: "Even"

identify_number_type(7)
# Output: "Odd"

identify_range(1, 3)
# Output: ["Odd", "Even", "Odd"]

identify_range(2, 6)
# Output: ["Even", "Odd", "Even", "Odd", "Even"]
```
## Transition from C to Python
In C, you might write:
```c
for (int i = start; i <= end; i++) {
    if (i % 2 == 0) {
        printf("Even\n");
    } else {
        printf("Odd\n");
    }
}
```
In Python, the same logic is simpler:
```python
for i in range():
    if logic:
        print("Even")
    else:
        print("Odd")
```

## How to check your solution
1. Open CLI and navigate to the assignment folder.
2. Run Python and import your functions:
   `from student_code_3_2 import *`
3. Call `identify_number_type(n)` or `identify_range(start, end)`.

## How to Run Autograder
1. Save your solution in `student_code_3_2.py`.
2. Run:
   `python autograder_3_2.py`
   or
   `python3 autograder_3_2.py`
3. Check your score, feedback, and Token.

## Notes
- Use conditional statements (`if/else`) and loops (`for`).
- Do not change file or function names.
- Submit your Token and screenshot in the Excel sheet/Google Form.