# Practical 5 – Task 4: Using a Debugger

## Objective
Demonstrate the use of a Python debugger (pdb or IDE debugger) on a sample program with intentional errors. Learn how to set breakpoints, step through code, and examine variable values.

## Instructions
- Open `student_code_5_4.py`.
- The function `buggy_function()` contains intentional errors
- Run the program with a debugger.
- Use breakpoints and step through the code.
- Inspect variable values at each step.
- Identify the errors and fix them.

## Example with pdb
To run the debugger, you can use:

```
import pdb  
import student_code_5_4  
pdb.run('student_code_5_4.buggy_function()')
```
or directly from the terminal (recommended)
```
python3 -m pdb student_code_5_4.py
```
Common commands:
- break buggy_function → set breakpoint
- step → step into function
- next → execute next line
- print x → inspect variable
- continue → resume execution

## Transition from C to Python
In C, debugging is often done with gdb or IDE debuggers.  
In Python, pdb and IDE tools provide similar functionality.

## How to check your solution
- Run `autograder_5_4.py`.
- The autograder verifies that `buggy_function` exists.
- Debugging must be demonstrated manually in class.

## Notes
- Do not remove `buggy_function`; it is required for demonstration.
- Submit your token and screenshot in the Excel sheet.