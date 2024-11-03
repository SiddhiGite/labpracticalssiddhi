def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1 or (col - row + i >= 0 and board[i][col - row + i] == 1) or (col + row - i < n and board[i][col + row - i] == 1):
            return False
    return True

def solve_nqueens(board, row, n):
    if row == n:
        return True
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_nqueens(board, row + 1, n):
                return True
            board[row][col] = 0
    return False

def n_queens_with_first_queen(n, first_row, first_col):
    board = [[0] * n for _ in range(n)]
    board[first_row][first_col] = 1
    if solve_nqueens(board, first_row + 1, n):
        print("Solution found:")
        print_board(board)
    else:
        print("No solution exists.")

n = int(input("Enter board size (n): "))
first_row = int(input("Enter first queen's row (0 to n-1): "))
first_col = int(input("Enter first queen's col (0 to n-1): "))

if 0 <= first_row < n and 0 <= first_col < n:
    n_queens_with_first_queen(n, first_row, first_col)
else:
    print("Invalid first queen position.")
