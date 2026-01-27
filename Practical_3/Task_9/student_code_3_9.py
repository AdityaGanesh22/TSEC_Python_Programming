# Rno: <student roll number>
# student_code_3_9.py

# Interactive Guessing Game
# The program should generate a random number once per game.
# The user must call start_game() to begin a new game.

# HINT: You will need a variable that stores the secret number.
#       This variable should be remembered across function calls.

# Function: start_game()
# - Generate a random number between 1 and 100
# - Store it in the secret number variable
# - Print: "A new game has started! Guess the number between 1 and 100."

import random

_secret_number = None

def start_game():
    """Start a new game by generating a random number."""
    global _secret_number
    # TODO: generate random number '_secret_number' and store it
    # TODO: print("A new game has started! Guess the number between 1 and 100.")
    pass

# Function: guessing_game()
# - If no game has started, print:
#   "No game in progress. Please call start_game() first."
# - Otherwise:
#   * Keep asking the user for guesses until they are correct
#   * If guess < secret number, print("Too low! Try again.")
#   * If guess > secret number, print("Too high! Try again.")
#   * If guess == secret number, print("Correct! The number was", secret number)

def guessing_game():
    """Run the guessing loop until the user guesses correctly."""
    global _secret_number
    if _secret_number is None:
        print("No game in progress. Please call start_game() first.")
        return

    guess = None
    # TODO: Use a while loop here
    # guess = int(input("Enter your guess: "))
    # TODO: if statements here to compare guess with _secret_number
    pass


