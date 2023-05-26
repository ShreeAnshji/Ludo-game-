import random

# Initialize the game board
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Initialize the players
players = {
    "R": [(3, 3), (3, 4), (4, 3), (4, 4)],
    "B": [(3, 0), (4, 0), (3, 1), (4, 1)],
    "G": [(0, 3), (0, 4), (1, 3), (1, 4)],
    "Y": [(0, 0), (0, 1), (1, 0), (1, 1)]
}

# Define the move function
def move(player, piece, steps):
    # Get the current position of the piece
    row, col = players[player][piece]
    
    # Calculate the new position of the piece
    new_row, new_col = row, col
    if row == 0:
        new_col += steps
        if new_col > 7:
            new_row += new_col // 8
            new_col %= 8
    elif row == 7:
        new_col -= steps
        if new_col < 0:
            new_row -= abs(new_col) // 8 + 1
            new_col = 8 - abs(new_col) % 8
    elif col == 0:
        new_row -= steps
        if new_row < 0:
            new_col += abs(new_row) // 8 + 1
            new_row = 8 - abs(new_row) % 8
    elif col == 7:
        new_row += steps
        if new_row > 7:
            new_col -= new_row // 8
    
    # Check if the new position is valid and update the game state
    if is_valid_move(player, piece, new_row, new_col):
        players[player][piece] = (new_row, new_col)
        board[row][col] = 0
        board[new_row][new_col] = player
        return True
    else:
        return False

# Define a function to check if a move is valid
def is_valid_move(player, piece, row, col):
    # Check if the new position is within the bounds of the board
    if row < 0 or row > 7 or col < 0 or col > 7:
        return False
    
    # Check if the new position is occupied by another piece of the same player
    if board[row][col] == player:
        return False
    
    # Check if the new position is occupied by a piece of another player
    for p, positions in players.items():
        for i, (r, c) in enumerate(positions):
            if p != player and r == row and c == col:
                return False
    
    return True

# Define a function to display the game board
def display_board():
    for row in board:
        print(row)

# Define a function to switch turns between players
def switch_turn(player):
    if player == "R":
        return "B"
    elif player == "B":
        return "G"
    elif player == "G":
        return "Y"
    else:
        return "R"

# Main game loop
def play_game():
    current_player = random.choice(list(players.keys()))

    while True:
        print("Current Player:", current_player)
        display_board()

        # Get user input for the move
        piece = int(input("Select a piece (0-3): "))
        steps = int(input("Enter the number of steps (1-6): "))

        # Perform the move
        if move(current_player, piece, steps):
            current_player = switch_turn(current_player)
        else:
            print("Invalid move! Try again.")

        print("\n---\n")

# Start the game
play_game()
