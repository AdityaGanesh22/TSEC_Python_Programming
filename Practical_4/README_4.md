# README_4 – Practical 4 Overview

Practical 4 introduces advanced Python concepts that build upon earlier fundamentals. The tasks in this practical focus on **file handling**, **data processing**, and **creating executable programs**. This README provides a conceptual overview so that students can directly attempt the tasks with confidence.


## File Handling – Reading and Writing Files


File handling allows programs to persist data beyond runtime. Python provides simple yet powerful tools for working with files.

- **Opening files**
  - `open(filename, mode)` where mode can be:
    - `"r"`: read
    - `"w"`: write (overwrites existing file)
    - `"a"`: append
    - `"r+"`: read and write
  - Always close files after use, or use `with open(...) as f:` which ensures
    automatic closing.

- **Reading files**
  - `f.read()` returns the entire file as a string.
  - `f.readline()` reads one line at a time.
  - `f.readlines()` returns a list of all lines.

- **Writing files**
  - `f.write("text")` writes a string to the file.
  - `f.writelines(list_of_strings)` writes multiple lines.

- **Splitting text into words**
  - Use `text.split()` to break content into words separated by whitespace.
  - Useful for tasks like extracting words of specific lengths.

- **Exception handling in file I/O**
  - Files may not exist or may be inaccessible.
  - Use `try/except` to handle errors gracefully:
    ```python
    try:
        with open("data.txt", "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("File not found")
    ```


## Creating Python Packages, Modules, and Executable Files

Python programs can be organized and distributed in different ways.

- **Modules**
  - A module is simply a `.py` file containing functions or classes.
  - Import with `import module_name` or `from module_name import function`.

- **Packages**
  - A package is a directory containing multiple modules and an `__init__.py` file.
  - Allows grouping related functionality together.
  - Example structure:
    ```
    mypackage/
        __init__.py
        module1.py
        module2.py
    ```

- **Executable files**
  - Python scripts normally require the interpreter to run.
  - Tools like **PyInstaller** can package scripts into standalone executables.
  - Steps:
    1. Install PyInstaller: `pip install pyinstaller`
    2. Run: `pyinstaller --onefile myscript.py`
    3. The executable appears in the `dist/` folder.
  - This is useful for distributing programs to users who do not have Python installed.


## Dealing with Errors and Scientific Debugging

Errors are inevitable in programming. Understanding their types and how to debug systematically is crucial.

- **Syntax Errors**
  - Occur when code violates Python’s grammar rules.
  - Example: missing colon, unmatched parentheses.
  - Python reports the line and type of syntax error.

- **Runtime Errors**
  - Occur while the program is running.
  - Examples: division by zero, accessing a missing file, invalid type conversion.
  - Use `try/except` blocks to catch and handle runtime errors.

- **Logical Errors**
  - Program runs without crashing but produces incorrect results.
  - Harder to detect; requires careful testing and validation.

- **Scientific Debugging Approach**
  - **Isolate**: Narrow down where the error occurs.
  - **Instrument**: Add print statements or logging to observe variable states.
  - **Hypothesize**: Form a theory about the cause.
  - **Test**: Modify code and rerun to confirm.
  - **Iterate**: Repeat until the bug is resolved.
  - Use tools like `pdb` (Python debugger) or IDE debuggers for step-by-step execution.


## Concepts Reinforced by Practical 4 Tasks

- **Task 1 (Extracting Words)**: Reinforces file reading, string splitting, and filtering.
- **Task 2 (Closest Points in 3D)**: Introduces CSV parsing, numerical computation, and nested loops.
- **Task 3 (Sorting City Names)**: Combines file reading, sorting algorithms, and file writing.
- **Task 4 (Executable Files)**: Demonstrates packaging Python scripts into standalone executables.

## Additional Notes


- Always validate input data before processing.
- Handle exceptions gracefully to avoid program crashes.
- Organize code into functions and modules for clarity and reuse.
- Use comments and docstrings to explain logic.
- Test programs with different inputs, including edge cases.
- Remember that debugging is a scientific process: observe, hypothesize, test, and refine.

## Summary


Practical 4 equips students with skills to:
- Work with text and CSV files.
- Apply exception handling for robustness.
- Organize code into modules and packages.
- Create executable files for distribution.
- Debug programs scientifically.

By mastering these concepts, students will be able to confidently tackle real-world data processing tasks and deliver programs that are both reliable and distributable.