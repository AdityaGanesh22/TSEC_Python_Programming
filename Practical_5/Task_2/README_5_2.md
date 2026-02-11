# Practical 5 – Task 2: Custom Exceptions in Banking System

## Objective
Develop a Python program that simulates a banking system with a withdraw function.
Raise custom exceptions for scenarios such as insufficient funds and invalid account numbers.

## Instructions
- Implement `withdraw(account_number, amount)` in `student_code_5_2.py`.
- Define two custom exceptions:
  - `InsufficientFundsError`
  - `InvalidAccountError`
- Use a dictionary to simulate accounts and balances.
- The function should:
  - `Raise InvalidAccountError` if account number does not exist.
  - `Raise InsufficientFundsError` if balance is less than withdrawal amount.
  - Deduct the amount and print the new balance if successful.

## Example
```
accounts = {"12345": 1000.0, "67890": 500.0}
```
Input:
`withdraw("12345", 200)`
Output:
`Withdrawal successful. New balance: 800.0`

Input:
`withdraw("00000", 100)`
Output:
`InvalidAccountError: Invalid account number.`

Input
`withdraw("67890", 1000)`
Output:
`InsufficientFundsError: Insufficient funds.`

## Transition from C to Python
In C, error handling is often done with return codes or flags.
In Python, custom exceptions provide a clean and readable way to handle specific error scenarios.

## How to check your solution
1. Save your solution in `student_code_5_2.py`.
2. Run `autograder_5_2.py`.
3. Check your score, feedback, and token.

## Notes
- Do not change the exception class names.
- Ensure withdraw() prints the new balance when successful.
- Submit your token and screenshot in the Excel sheet.