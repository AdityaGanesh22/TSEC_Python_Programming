# Rno: <student roll number>
# student_code_5_2.py

# Custom Exceptions in Banking System
# Program should simulate a banking system with a withdraw function.
# Raise custom exceptions for insufficient funds and invalid account numbers.

# Define custom exceptions
class InsufficientFundsError(Exception):
    pass

class InvalidAccountError(Exception):
    pass

# Dictionary to simulate accounts
accounts = {
    "12345": 1000.0,
    "67890": 500.0
}

def withdraw(account_number, amount):
    # TODO: Check if account_number exists
    # TODO: If not, raise InvalidAccountError
    # TODO: If balance < amount, raise InsufficientFundsError
    # TODO: Otherwise, deduct amount and print new balance
    pass