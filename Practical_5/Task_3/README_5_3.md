# Practical 5 – Task 3: Logging for Debugging

## Objective
Enhance a Python program by adding logging statements to record the flow of execution and error messages. Use the logging module to configure different logging levels (INFO, DEBUG, ERROR).

## Instructions
- Configure logging using the logging module.
- Add logging statements at different levels:
  - INFO: To record when functions are called.
  - DEBUG: To record successful execution details.
  - ERROR: To record error conditions.
- Implement the function divide_numbers(a, b):
  - Log when the function is called.
  - Log successful division.
  - Log division by zero errors.
  - Return the result or None if an error occurs.
- Do not remove or rename the required function.

## Example (General Demonstration)
```python
import logging

def multiply_numbers(a, b):
    logging.info("Function multiply_numbers called")
    try:
        result = a * b
        logging.debug("Multiplication successful")
        return result
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return None
```
## Notes
- Ensure log messages match exactly what is expected by the autograder.
- Do not configure logging globally; let the autograder capture logs.
- Return values instead of printing them.