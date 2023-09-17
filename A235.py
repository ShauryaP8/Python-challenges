# Function to check if it is safe to place a queen at board[row][col]
def is_safe(board, row, col, N):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper diagonal on right side
    i = row
    j = col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

# Recursive function to solve the N-Queens problem
def solve_n_queens(board, row, N):
    # Base case: if all queens are placed, return True
    if row == N:
        return True

    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            # Place the queen
            board[row][col] = 1

            # Recur for the next row
            if solve_n_queens(board, row + 1, N):
                return True

            # If placing the queen leads to a solution, return True
            # Otherwise, backtrack and remove the queen from the current cell
            board[row][col] = 0

    # If the queen cannot be placed in any column of the current row, return False
    return False

# Function to print the chessboard
def print_board(board, N):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

# Main function to solve the N-Queens problem
def n_queens(N):
    board = [[0] * N for _ in range(N)]
    if solve_n_queens(board, 0, N):
        print_board(board, N)
    else:
        print("Not possible")

# Example usage
n_queens(4)
