# Tic Tac Toe Game
1

import random
def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])

def input_player(board):
    choice1 = int(input("First player enter a number(0-8)"))
    if board[choice1] == "-":
        board[choice1] = "X"
    choice2 = int(input("Second player eneter a number(0-8)"))
    if board[choice2] == "-":
        board[choice2] = "O"

def computer(board):
    choice = int(input("Enter a number"))
    if board[choice] == "-":
        board[choice] = "X"
    num = random.randint(0,8)
    if board[num] == "-":
        board[num] = "O"

def win(board):
    if board[0] == board[1] == board[2] and board[0] == "X" and board[0] != "-":
        printboard(board)
        print("X wins")
        return True
    elif  board[3] == board[4] == board[5] and board[3] == "X" and board[3] != "-":
        printboard(board)
        print("X wins")
        return True
    elif board[6] == board[7] == board[8] and board[6] == "X" and board[6] != "-":
        printboard(board)
        print("X wins")
        return True
    elif board[0] == board[3] == board[6] and board[0] == "X" and board[0] != "-":
        printboard(board)
        print("X wins")
        return True
    elif board[1] == board[4] == board[7] and board[1] == "X" and board[1] != "-":
        printboard(board)
        print("X wins")
        return True
    elif board[2] == board[5] == board[8] and board[2] == "X" and board[2] != "-":
        printboard(board)
        print("X wins")
        return True
    elif board[0] == board[4] == board[8] and board[0] == "X" and board[0] != "-":
        printboard(board)
        print("X wins")
        return True
    elif board[2] == board[4] == board[6] and board[2] == "X" and board[2] != "-":
        printboard(board)
        print("X wins")
        return True
    elif board[0] == board[1] == board[2] and board[0] == "O" and board[0] != "-":
        printboard(board)
        print("O wins")
        return True
    elif  board[3] == board[4] == board[5] and board[3] == "O" and board[3] != "-":
        printboard(board)
        print("O wins")
        return True
    elif board[6] == board[7] == board[8] and board[6] == "O" and board[6] != "-":
        printboard(board)
        print("O wins")
        return True
    elif board[0] == board[3] == board[6] and board[0] == "O" and board[0] != "-":
        printboard(board)
        print("O wins")
        return True
    elif board[1] == board[4] == board[7] and board[1] == "O" and board[1] != "-":
        printboard(board)
        print("O wins")
        return True
    elif board[2] == board[5] == board[8] and board[2] == "O" and board[2] != "-":
        printboard(board)
        print("O wins")
        return True
    elif board[0] == board[4] == board[8] and board[0] == "O" and board[0] != "-":
        printboard(board)
        print("O wins")
        return True
    elif board[2] == board[4] == board[6] and board[2] == "O" and board[2] != "-":
        printboard(board)
        print("O wins")
        return True
2


board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
print("Do you want to play with computer or multiplayer(1 for cmputer and 2 for multiplayer)1")
option = int(input())
if option  == 2:
    player1 = "X"
    print("Player 1 is X and player 2 is O")
    player2 = "O"
    while True:
        printboard(board)
        input_player(board)
        if win(board):
            break
        continue
if option == 1:
    print("You are X and computer is O")
    player = "X"
    while True:
        printboard(board)
        computer(board)
        if win(board):
            break
        continue
