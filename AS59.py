def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
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
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")

    while True:
        print_board(board)
        print(f"Player {current_player}, enter your move (row and column): ")
        try:
            row, col = map(int, input().split())
            if board[row][col] == " ":
                board[row][col] = current_player

                if check_winner(board, current_player):
                    print_board(board)
                    print(f"Player {current_player} wins!")
                    break
                elif is_board_full(board):
                    print_board(board)
                    print("It's a tie!")
                    break
                else:
                    current_player = "O" if current_player == "X" else "X"
            else:
                print("That cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as integers.")

if __name__ == "__main__":
    main()
