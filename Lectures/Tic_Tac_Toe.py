# We will be creating a game on python (X and O/Tic-tac-toe)
# This will summarize what we have learnt till now
# Major topics to be covered: Lists, loops, if-else, inputs
import random 

# Print a grid
def call_grid(block):
    print(block[0] + ' | ' + block[1] + ' | ' + block[2])
    print("--+---+--")
    print(block[3] + ' | ' + block[4] + ' | ' + block[5])
    print("--+---+--")
    print(block[6] + ' | ' + block[7] + ' | ' + block[8] + "\n")


# Initialize the game board with numbers 1-9
block = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Randomly decide who starts first (X or O)
player = random.choice(["X", "O"])
print(f"Player {player} starts first!\n")

# Track which cells have been used
check_list = []

# Display the initial empty board
call_grid(block)

# Main game loop - run for maximum 9 turns
for i in range(9):
    # Get input from human player (X) or random move for computer (O)
    if player == "X":
        value = int(input("Which cell would you like to enter?: "))
    elif player == "O":
        value = random.randrange(1, 10)
    
    # Keep asking for input if the chosen cell is already taken
    while value in check_list:
        if player == "X":
            value = int(input("Which cell would you like to enter?: "))
        elif player == "O":
            value = random.randrange(1, 10)
    
    # Record the move and update the board
    check_list.append(value)
    block[value - 1] = player
    call_grid(block)
    
    # Check if current player has won
    if ((block[0] == block[1] == block[2]) or 
        (block[3] == block[4] == block[5]) or 
        (block[6] == block[7] == block[8]) or 
        (block[0] == block[3] == block[6]) or 
        (block[1] == block[4] == block[7]) or 
        (block[2] == block[5] == block[8]) or 
        (block[0] == block[4] == block[8]) or 
        (block[2] == block[4] == block[6])):
        print("Player " + player + " wins!!!")
        break
    elif i == 8:
        print("The game is a draw")
    
    # Switch to the other player
    if player == "X":
        player = "O"
    else:
        player = "X"

