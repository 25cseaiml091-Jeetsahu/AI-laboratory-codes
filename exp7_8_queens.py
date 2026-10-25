N=8
def print_board(board):
    for row in board:
        print(" ".join("Q" if col == 1 else "." for col in row))
def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True
def solve_nqueens(board, col):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_nqueens(board, col + 1):
                return True
            board[i][col] = 0
    return False
if __name__ == '__main__':
    board = [[0] * N for _ in range(N)]
    if solve_nqueens(board, 0):
        print_board(board)
    else:
        print("No solution exists")
""" OUTPUT:
Q . . . . . . .
. . . . . . Q .
. . . . Q . . .
. . . . . . . Q
. Q . . . . . .
. . . Q . . . .
. . . . . Q . .
. . Q . . . . .
                  """
