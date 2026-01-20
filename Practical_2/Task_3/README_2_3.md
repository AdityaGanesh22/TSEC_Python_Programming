# Practical 2 – Task 3: Student Record Keeper

## Objective
Write Python functions to manage student records using dictionaries.

## Instructions
Implement the following functions in `student_code_2_3.py`:
1. `create_record(records, name, grade, attendance)`
   - Adds a new student record.
2. `update_grade(records, name, new_grade)`
   - Updates the grade of a student.
3. `update_attendance(records, name, new_attendance)`
   - Updates the attendance of a student.
4. `delete_record(records, name)`
   - Removes a student record.

## Examples
```python
create_record({}, "Aditi", "A", 90)
# Output: {"Aditi": {"grade": "A", "attendance": 90}}

update_grade({"Rahul": {"grade": "B", "attendance": 85}}, "Rahul", "A")
# Output: {"Rahul": {"grade": "A", "attendance": 85}}

update_attendance({"Sneha": {"grade": "C", "attendance": 70}}, "Sneha", 95)
# Output: {"Sneha": {"grade": "C", "attendance": 95}}

delete_record({"Karan": {"grade": "B", "attendance": 80}}, "Karan")
# Output: {}
```

## How to check your solution
1. Open CLI and navigate to the assignment folder.
2. Run Python and import your functions:
   `from student_code_2_3 import *`
3. Test your functions interactively.

## How to Run Autograder
1. Save your solution in `student_code_2_3.py`.
2. Run:
   `python autograder_2_3.py`
   or
   `python3 autograder_2_3.py`
3. Check your score, feedback, and Token.

## Notes
- Use only basic dictionary operations (assignment, update, delete).
- Do not change file or function names.
- Submit your Token in the Excel sheet/Google Form and retain the screenshot of this with you.