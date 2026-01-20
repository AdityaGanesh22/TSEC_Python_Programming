# Practical 2 – Task 2: Student Enrollment Manager

## Objective
Demonstrate the use of sets in Python to manage student enrollments in multiple courses or exams.

## Instructions
Implement the following functions in `student_code_2_2.py`:
1. `union_enrollments(set1, set2)`
   - Returns all students in either set1 or set2.
2. `intersection_enrollments(set1, set2)`
   - Returns students common to both sets.
3. `difference_enrollments(set1, set2)`
   - Returns students in set1 but not in set2.

## Examples
```python
CET = {"Aditi", "Rahul", "Sneha"}
JEE = {"Rahul", "Sneha", "Karan"}
NEET = {"Aditi", "Karan", "Meera"}

union_enrollments(CET, JEE)
# Output: {"Aditi", "Rahul", "Sneha", "Karan"}

intersection_enrollments(CET, JEE)
# Output: {"Rahul", "Sneha"}

difference_enrollments(CET, JEE)
# Output: {"Aditi"}

union_enrollments(JEE, NEET)
# Output: {"Rahul", "Sneha", "Karan", "Aditi", "Meera"}

intersection_enrollments(JEE, NEET)
# Output: {"Karan"}

difference_enrollments(NEET, CET)
# Output: {"Karan", "Meera"}
```
## How to check your solution
1. Open CLI and navigate to the assignment folder.
2. Run Python and import your functions:
   `from student_code_2_2 import *`
3. Test your functions interactively.

## How to Run Autograder
1. Save your solution in `student_code_2_2.py.`
2. Run:
   `python autograder_2_2.py`
   or
   `python3 autograder_2_2.py`
3. Check your score, feedback, and Unique ID.

## Notes
- Use only basic set methods (union, intersection, difference).
- Do not change file or function names.
- Submit your Token in the Excel sheet/Google Form and retain the screenshot of this with you