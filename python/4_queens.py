# 4_queens.py

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i] == 'q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'q':
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 'q':
            return False

    return True

def solve_n_queens_util(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 'q'
            if solve_n_queens_util(board, col + 1):
                return True
            board[i][col] = 0

    return False

def solve_n_queens():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False

    print_solution(board)
    return True

def print_solution(board):
    for row in board:
        print(" ".join(str(x) for x in row))

if __name__ == "__main__":
    solve_n_queens()