# Practical 3 – Task 3: Character Type Identifier

## Objective
Create a Python program to check whether the given input is a digit, lowercase character, uppercase character, or a special character using an if-else-if ladder.

## Instructions
- Implement the function identify_character(ch) in student_code_3_3.py.
- The function should return one of:
  - "Digit"
  - "Lowercase"
  - "Uppercase"
  - "Special"

## Examples
```python
identify_character("5")
# Output: "Digit"

identify_character("a")
# Output: "Lowercase"

identify_character("Z")
# Output: "Uppercase"

identify_character("@")
# Output: "Special"
```

## Transition from C to Python
In C, you might write:
```c
if (ch >= '0' && ch <= '9') {
    printf("Digit");
} else if (ch >= 'a' && ch <= 'z') {
    printf("Lowercase");
} else if (ch >= 'A' && ch <= 'Z') {
    printf("Uppercase");
} else {
    printf("Special");
}
```


## How to check your solution
1. Open CLI and navigate to the assignment folder.
2. Run Python and import your function:
   `from student_code_3_3 import *`
3. Call `identify_character(ch)` with different inputs.

## How to Run Autograder
1. Save your solution in `student_code_3_3.py`.
2. Run:
   `python autograder_3_3.py`
   or
   `python3 autograder_3_3.py`
3. Check your score, feedback, and Token.

## Notes
- Use an if-else-if ladder.
- Do not change file or function names.
- Submit your Token and screenshot in the Excel sheet/Google Form.