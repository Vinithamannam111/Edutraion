AI_PLAYER = 'X'
HUMAN_PLAYER = 'O'
EMPTY = '_'

# Check if there are any moves left
def has_moves(board):
    return any(cell == EMPTY for row in board for cell in row)

# Evaluate the board and return a score
def score_board(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return 10 if row[0] == AI_PLAYER else -10

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return 10 if board[0][col] == AI_PLAYER else -10

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return 10 if board[0][0] == AI_PLAYER else -10

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return 10 if board[0][2] == AI_PLAYER else -10

    return 0

# Minimax algorithm
def minimax(board, is_max_turn, depth):
    current_score = score_board(board)

    if current_score in [10, -10]:
        return current_score
    if not has_moves(board):
        return 0

    if is_max_turn:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI_PLAYER
                    eval = minimax(board, False, depth + 1)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN_PLAYER
                    eval = minimax(board, True, depth + 1)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
        return min_eval


def get_best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI_PLAYER
                move_val = minimax(board, False, 0)
                board[i][j] = EMPTY

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)

    print("Best move score evaluated as:", best_val)
    return best_move


game_board = [
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['', '', '_']
]

best_move = get_best_move(game_board)
print(f"The AI recommends placing at ROW: {best_move[0]}, COL: {best_move[1]}")