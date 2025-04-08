import numpy as np

fit = input("Enter 1st player name: ")
snd = input("Enter 2nd player name: ")

fps = "x"
sps = "o"

board = np.array([["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]])

def turn(player, symbol):
    print(player, "'s turn:")
    
    r = int(input("Enter row number (1, 2, or 3): ")) - 1
    c = int(input("Enter column number (1, 2, or 3): ")) - 1
    insert(r, c, player, symbol)

def insert(row, col, player, symbol):
    if row not in [0, 1, 2] or col not in [0, 1, 2]:
        print("Invalid position! Choose a number between 1 and 3.")
        turn(player, symbol)
        return

    if board[row][col] != "-":
        print("Box already filled! Choose another spot.")
        turn(player, symbol)
        return

    board[row][col] = symbol
    print("Current board:")
    for i in board:
        print(i)

def check_row(symbol):
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] == symbol:
            return True
    return False

def check_col(symbol):
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] == symbol:
            return True
    return False

def check_diag(symbol):
    return (board[0][0] == board[1][1] == board[2][2] == symbol) or (board[0][2] == board[1][1] == board[2][0] == symbol)

def won(symbol):
    return check_row(symbol) or check_col(symbol) or check_diag(symbol)

def play():
    for i in range(9):
        if i % 2 == 0:
            turn(fit, fps)
            if won(fps):
                print("Player", fit, "won the match!")
                return 
        else:
            turn(snd, sps)
            if won(sps):
                print("Player", snd, "won the match!")
                return  

    print("It's a draw!")  

play()