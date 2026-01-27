# Practical 3 – Task 9: Interactive Guessing Game

## Objective
Develop a number guessing game where the program generates a random number only once per game.
The user must explicitly call `start_game()` to begin a new game.

## Instructions
- Implement two functions in `student_code_3_9.py`:
  - `start_game()`: generates a new random number between 1 and 100 and announces the start of the game.
  - `guessing_game()`: runs the guessing loop until the correct number is guessed.
- The random number should persist across guesses until `start_game()` is called again.

## Example Run
```python
>>> start_game()
A new game has started! Guess the number between 1 and 100.
Enter your guess: 50
Too low! Try again.
Enter your guess: 75
Too high! Try again.
Enter your guess: 63
Correct! The number was 63

>>> start_game()
A new game has started! Guess the number between 1 and 100.
Enter your guess: ...
```

## Key Concepts
- **Global variables** can store state across function calls.
- **Functions** modularize logic (start vs guessing).
- **Loops and conditionals** handle repeated guesses and feedback.
- **Error handling** ensures invalid inputs don’t crash the program.

## How to check your solution
1. Save your solution in `student_code_3_9.py`.
2. Run Python and import your functions:
   `from student_code_3_9 import *`
3. Call `start_game()` to generate a number.
4. Call `guessing_game()` to play.

## How to Run Autograder
1. Save your solution in `student_code_3_9.py`.
2. Run:
   `python autograder_3_9.py`
   or
   `python3 autograder_3_9.py`
3. Check your score, feedback, and token.

## Notes
- Random number is generated only once per game.
- Submit your Unique ID and screenshot in the Excel sheet.