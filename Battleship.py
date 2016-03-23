#Written for Pyzo 3.4.1

from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(input("Guess Row:"))
guess_col = int(input("Guess Col:"))

def showship():
    print("Ship Row: "+ str(ship_row))
    print("Ship Col: "+ str(ship_col))
    return
showship()
# Write your code below!
def hitmarker():
    if guess_col==ship_col and guess_col==ship_col:
        print("Congratulations! You sank my battleship!")
    else:
        print("You missed my battleship!")
        board[guess_row][guess_col]="X"
    return
hitmarker()
print_board(board)