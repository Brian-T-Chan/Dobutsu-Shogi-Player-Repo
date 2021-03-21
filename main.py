# Brian Chan
# March 2021

# This program, main.py, is the main user interface.

from board import initialstate, capturewin, noncapturewin
from board_display import display
from board_input import enter, commandinstructions
from alphabeta import alphabeta

# Constants indicating the players involved.
a, b = 'A', 'B'

# The user controls Player A and the program controls Player B. Player A is
# the ''south'' player (the player controlling the pieces l, g, e, c below) and
# Player B is the ''north'' player controlling the pieces L, G, E, C below).
#
# Initial position of the game:
# ---------------
# ---------------
#    1   2   3
# 1  G   L   E
# 2  *   C   *
# 3  *   c   *
# 4  e   l   g
# ---------------
# ---------------

# This function runs during Player A's turn.

def playerA(board1):
    command = input("Your turn: ")
    board2 = enter(a, command, board1)

    if board2 is None:
        print("Press enter to exit the game.")
        input()
        quit()
    else:
        display(board2)

    lioncapture2 = capturewin(board2)
    lioncross2 = noncapturewin(board2)

    if lioncapture2 == a:
        print("Player A has won the game. Enter to exit.")
        input()
        quit()

    if lioncross2 == a:
        print("Player A has won the game. Enter to exit.")
        input()
        quit()

    elif lioncross2 == b:
        print("Player B has won the game. Enter to exit.")
        input()
        quit()

    return board2

# This function runs during Player B's turn.

def playerB(board2, ply):
    print('Thinking ...')

    board1 = alphabeta(board2, ply)

    display(board1)

    lioncapture1 = capturewin(board1)
    lioncross1 = noncapturewin(board1)

    if lioncapture1 == b:
        print("Player B has won the game. Enter to exit.")
        input()
        quit()

    if lioncross1 == b:
        print("Player B has won the game. Enter to exit.")
        input()
        quit()

    elif lioncross1 == a:
        print("Player A has won the game. Enter to exit.")
        input()
        quit()

    return board1

# Asks the user if he/she wants to learn about the game controls.

def commandsquery():
    print()
    print("To move or drop the pieces, this program uses specific commands.")
    while True:
        learn = input("Learn about these commands? (enter 1 for yes and 0 " +
        "for no): ")
        try:
            learn = int(learn)
        except:
            print("Invalid input, try again.")
            continue
        if learn == 1:
            message = commandinstructions()
            print(message)
            break
        if learn == 0:
            break

# Asks the user about who should make the first move.
            
def orderquery():
    while True:
        print()
        first = input("Who should play first (enter 0 if the user should play first \n"+\
        "and enter 1 if the program should play first: " )
        try:
            first = int(first)
        except:
            print("Invalid input, try again.")
            continue
        if first == 0 or first == 1:
            break
    return first

# Asks the user for the level of difficulty the machine should play at.

def levelquery():
    while True:
        print()
        print("SET LEVEL OF DIFFICULTY (Level 1 is easiest, Level 5 is hardest.)")
        print("Level 1 (3 ply)")
        print("Level 2 (4 ply)")
        print("Level 3 (5 ply)")
        print("Level 4 (6 ply)")
        print("Level 5 (7 ply)")
        level = input("Enter 1 for Level 1, 2 for Level 2, ..., and 5 for" +\
        " Level 5: ")
        try:
            level = int(level)
        except:
            print("Invalid input, try again.")
            continue
        if 1 <= level <= 5:
            break

    return level + 2

# Runs the user interface.

def main():
    print()
    print("** DOBUTSU SHOGI PLAYER **")
    print("Brian Chan - 2021")
    print()

    print("Welcome. This program plays a variant of Shogi known as Dobutsu")
    print("Shogi (also known as Animal Shogi), a game invented by Madoka")
    print("Kitao.")

    commandsquery()
    first = orderquery()
    ply = levelquery()

    board = initialstate
    display(board)
    if first == 0:
        while True:
            brd = playerA(board)
            board = playerB(brd, ply)

    if first == 1:
        while True:
            brd = playerB(board, ply)
            board = playerA(brd)

if __name__ == '__main__':
    main()
