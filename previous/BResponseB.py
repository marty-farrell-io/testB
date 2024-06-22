def create_board():
    # Create and return a 3x3 tic-tac-toe board as a list of lists filled with spaces (indicating empty cells)
    return [[" " for _ in range(3)] for _ in range(3)]


def print_board(board):
    # Print the tic-tac-toe board with indices for user's convenience
    print("   1   2   3")
    for i, row in enumerate(board):
        print(i + 1, "|", " | ".join(row), "|")


def get_player_move(board):
    # Prompt the human player to enter their move as x, y coordinates, check for validity, and return the move
    while True:
        try:
            x, y = map(int, input("Enter coordinates (x, y): ").split(","))
            if 1 <= x <= 3 and 1 <= y <= 3 and board[y - 1][x - 1] == " ":
                return x - 1, y - 1
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid format. Please use x, y coordinates.")


def place_move(board, move, player):
    # Place the player's move ('X' or 'O') on the board
    board[move[1]][move[0]] = player


def check_win(board, player):
    # Check if the specified player has won the game
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    # Check if the board is full (no empty spaces left)
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True


def evaluate(board):
    # Evaluate the board from the AI's perspective ('O')
    if check_win(board, "O"):
        return 1  # AI wins
    elif check_win(board, "X"):
        return -1  # Human player wins
    else:
        return 0  # Tie or undecided


def minimax(board, depth, is_maximizing):
    # The minimax algorithm to calculate the best move for the AI
    score = evaluate(board)
    if score != 0 or is_board_full(board):
        return score

    if is_maximizing:
        # AI's turn: try to maximize the score
        best_score = -float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "O"
                    score = minimax(board, depth + 1, False)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        # Human's turn: minimize the score (assume the human player plays optimally)
        best_score = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = "X"
                    score = minimax(board, depth + 1, True)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score


def get_ai_move(board):
    # Use the minimax algorithm to find the best move for the AI
    best_score = -float("inf")
    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                score = minimax(board, 0, False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    best_move = (col, row)
    return best_move


def play_game():
    # Main function to play the game
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