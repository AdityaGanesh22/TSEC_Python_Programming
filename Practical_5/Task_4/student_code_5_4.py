# Rno: <student roll number>
# student_code_5_4.py

# Using a Debugger
# Demonstrate the use of a Python debugger (pdb or IDE debugger)
# on a sample program with intentional errors.

# Instructions for students:
# - This program contains intentional errors.
# - You should run it with a debugger (pdb or IDE).
# - Set breakpoints, step through code, and examine variable values.
# - Identify and fix the errors using the debugger.

def buggy_function():
    # Intentional errors:
    # 1. Variable 'x' is used before assignment.
    # 2. Division by zero.
    # 3. Incorrect type operation.
    
    print("Starting buggy function...")
    
    # TODO: Use debugger to step through and inspect variables
    result = x + 10   # Error: x not defined
    
    y = 0
    z = 5 / y         # Error: division by zero
    
    name = "Aditya"
    number = 10
    combined = name + number   # Error: cannot add str and int
    
    print("Result:", result)
    print("Combined:", combined)

# Students should run:
# import pdb; pdb.run('buggy_function()')
# or use IDE breakpoints to debug.