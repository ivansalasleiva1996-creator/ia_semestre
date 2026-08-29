WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)

def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def minimax_alphabeta(board, depth, alpha, beta, maximizing):
    """Minimax optimizado mediante Poda Alfa-Beta."""
    w = winner(board)
    if w == "X": return 1
    if w == "O": return -1
    if " " not in board: return 0
    
    if maximizing:
        max_eval = float('-inf')
        for i, cell in enumerate(board):
            if cell == " ":
                board[i] = "X"
                eval_val = minimax_alphabeta(board, depth + 1, alpha, beta, False)
                board[i] = " "
                max_eval = max(max_eval, eval_val)
                alpha = max(alpha, eval_val)
                if beta <= alpha:
                    break  # Poda Beta
        return max_eval
    else:
        min_eval = float('inf')
        for i, cell in enumerate(board):
            if cell == " ":
                board[i] = "O"
                eval_val = minimax_alphabeta(board, depth + 1, alpha, beta, True)
                board[i] = " "
                min_eval = min(min_eval, eval_val)
                beta = min(beta, eval_val)
                if beta <= alpha:
                    break  # Poda Alfa
        return min_eval

def best_move(board):
    best_val = float('-inf')
    move = -1
    for i, cell in enumerate(board):
        if cell == " ":
            board[i] = "X"
            move_val = minimax_alphabeta(board, 0, float('-inf'), float('inf'), False)
            board[i] = " "
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def print_board(b):
    print("\nTablero:")
    for i in range(0, 9, 3):
        print(f" {b[i]} | {b[i+1]} | {b[i+2]} ")
        if i < 6: print("---+---+---")

if __name__ == "__main__":
    board = ["X", "O", "X", "O", "X", " ", " ", " ", "O"]
    print("=" * 50)
    print("DECISIÓN MINIMAX CON PODA ALFA-BETA")
    print("=" * 50)
    print_board(board)
    pos = best_move(board)
    print(f"\nMejor posición calculada para 'X': {pos}")