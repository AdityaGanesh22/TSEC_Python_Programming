# Practical 5 – Comprehensive Concepts Guide

Practical 5 focuses on **exception handling, custom exceptions, logging, debugging, and scientific debugging techniques**. These skills are essential for writing robust, maintainable, and error‑free Python programs. This guide explains all the concepts required to complete Practical 5 independently, with illustrative examples that are related but not identical to the tasks.


## Basic Exception Handling


### What are exceptions?
Exceptions are events that disrupt the normal flow of a program. They occur when an error is detected during execution.

Common built‑in exceptions:
- `ZeroDivisionError` → dividing by zero
- `ValueError` → invalid type conversion
- `FileNotFoundError` → missing file
- `IndexError` → accessing out‑of‑range list index

### Handling exceptions
Use try/except blocks:
```python
try:
    x = int("abc")   # invalid conversion
except ValueError:
    print("Error: Invalid input")
```

You can also use finally to ensure cleanup:
```python
try:
    f = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("Execution completed")
```

## Custom Exceptions


### Why create custom exceptions?
Built‑in exceptions cover common errors, but sometimes you need domain‑specific errors. For example, in a banking system, you may want to raise InsufficientFundsError.

### Defining custom exceptions
```python
class InsufficientFundsError(Exception):
    pass

class InvalidAccountError(Exception):
    pass
```

### Raising custom exceptions
```python
def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Balance too low")
    return balance - amount
```


## Logging for Debugging

### Why use logging?
`print()` is useful for quick checks, but logging provides structured, configurable output. It allows you to record program flow, errors, and debug information.

### Logging levels
- `DEBUG` → detailed diagnostic info
- `INFO` → general program flow
- `WARNING` → potential issues
- `ERROR` → serious problems
- `CRITICAL` → severe errors

### Example
```python
import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

logging.info("Program started")
try:
    result = 10 / 0
except ZeroDivisionError:
    logging.error("Division by zero occurred")
```


## Using a Debugger

### pdb (Python Debugger)
Python includes a built‑in debugger called pdb. It allows you to pause execution, inspect variables, and step through code.

### Common commands
- `break <line>` → set breakpoint
- `step` → step into function
- `next` → execute next line
- `print <var>` → inspect variable
- `continue` → resume execution

### Example
```python
import pdb

def buggy_function():
    x = 5
    pdb.set_trace()   # execution stops here
    y = x / 0         # error line
```

You can use IDE debuggers (like VS Code or PyCharm) for a graphical interface.


## Scientific Debugging Techniques

### What is scientific debugging?
It is a systematic approach to finding and fixing bugs:
1. Isolate → narrow down where the error occurs.
2. Instrument → add print/logging statements to observe state.
3. Hypothesize → form a theory about the cause.
4. Test → modify code and rerun.
5. Iterate → repeat until resolved.

### Binary search debugging
- Comment out half the code and run.
- If the error disappears, the bug is in the commented section.
- If the error persists, the bug is in the active section.
- Narrow down further until the exact line is identified.

### Example
Suppose a loop crashes:
```python
numbers = [1, 2, 3]
for i in range(10):   # error: out of range
    print(numbers[i])
```

Debugging steps:
- Print `i` before accessing.
- Check length of list.
- Adjust loop to `range(len(numbers))`.

## Additional Notes


- Always validate inputs before processing.
- Use exceptions for error handling, not for normal control flow.
- Logging should be used instead of print for production code.
- Debuggers are powerful tools; learn to set breakpoints and inspect variables.
- Scientific debugging emphasizes methodical problem solving, not guesswork.
