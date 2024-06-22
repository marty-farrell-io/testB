# Creates a 3x3 Tic-Tac-Toe board
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Prints the current state of the board
def print_board(board):
    print("   1   2   3")
    for i, row in enumerate(board):
        print(i + 1, "|", " | ".join(row), "|")

# Gets a valid move from the player
def get_player_move(board):
    while True:
        try:
            x, y = map(int, input("Enter coordinates (x, y): ").split(","))
            if 1 <= x <= 3 and 1 <= y <= 3 and board[y - 1][x - 1] == " ":
                return x - 1, y - 1
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid format. Please use x, y coordinates.")

# Places a move on the board for a given player
def place_move(board, move, player):
    board[move[1]][move[0]] = player

# Checks if a player has won the game
def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Checks if the board is full
def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

# Evaluates the current state of the board
# Returns 1 if the AI wins, -1 if the player wins, and 0 otherwise
def evaluate(board):
    if check_win(board, "O"):  # AI wins
        return 1
    elif check_win(board, "X"):  # Player wins
        return -1
    else:
        return 0  # No winner

# Recursive minimax algorithm to determine the best move for the AI
# The AI (O) tries to maximize its score, while the player (X) tries to minimize it
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score != 0:  # Terminal state
        return score
    if is_board_full(board):
        return 0  # Draw

    if is_maximizing:  # AI's turn
        best_score = -float("inf")  # Initialize best score to negative infinity
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"  # Try a move
                    score = minimax(board, depth + 1, False)  # Recurse
                    board[row][col] = " "  # Undo the move
                    best_score = max(score, best_score)  # Update best score
        return best_score
    else:  # Player's turn
        best_score = float("inf")  # Initialize best score to positive infinity
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"  # Try a move
                    score = minimax(board, depth + 1, True)  # Recurse
                    board[row][col] = " "  # Undo the move
                    best_score = min(score, best_score)  # Update best score
        return best_score

# Use the minimax algorithm to determine the best move for the AI
def get_ai_move(board):
    best_score = -float("inf")  # Initialize best score to negative infinity
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"  # Try a move
                score = minimax(board, 0, False)  # Recurse
                board[row][col] = " "  # Undo the move
                if score > best_score:
                    best_score = score
                    best_move = (col, row)
    return best_move

# Main game loop
def play_game():
    board = create_board()
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            print(f"Player {current_player}'s turn.")
            move = get_player_move(board)
        else:
            print("AI's turn...") 
            move = get_ai_move(board)

        place_move(board, move, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board): 
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()