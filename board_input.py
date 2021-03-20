# Brian Chan
# March 2021

from board_hardware import perform
from board_display import convert

# Constants indicating the players involved.
a, b = 'A', 'B'

# The following program describes to the user how to input commands (move,
# promote, drop), it translates commands inputted by the player (to move a
# piece, promote a piece, or drop a piece), and it performs the translated
# command using board_hardware.py. It is an interface between the user and
# the programs board.py and board_hardware.py. The purpoe of this program is
# to allow the player to input commands without having to know the internal
# state of the data structures used to construct the game board and the pieces.
# The nature of the commands that can be inputted by the player is described in
# the commandinstructions() function shown below. However, to describe
# additional functionality this program has, we give an additional example.

# Given the following position, and assuming that it is Player B
# to move,

# Player B
#    1  2  3
# 1  *  *  L
# 2  g  E  C
# 3  C  e  *
# 4  *  l  g
# Player A

# Player B can input the command 'pc3141' to promote his/her chick, resulting
# in the following.

# Player B
#    1  2  3
# 1  *  *  L
# 2  g  E  C
# 3  *  e  *
# 4  H  l  g
# Player A

# The following function describes to the player how to make moves, promotions,
# and drops.

def commandinstructions():

    command_instructions = '''
USER INPUT INSTRUCTIONS:

The ranks (the rows) of the Dobutsu Shogi game board are numbered 1 through 4
from top to bottom. The files (the columns) of this board are numbered 1 through
3 from left to right. Squares are denoted (i,j) where i denotes the row number
of the row containing the square and where j denote the column number of the
column containing the square. Player A is the player whose pieces at the
beginning of the game are on squares (4,1), (4,2), (4,3), and (3,2). Player B is
the other player. The user controls Player A and the machine controls Player B.

Commands inputted by users are special strings that have to be one of the
following three forms (users inputting invalid commands will be given error
messages):

      mxijkl, pxijkl, dxij

The first letter indicates a move (m), promote (p), or drop action (d). The
second letter represents the type of the piece being considered:

l (lion), g (giraffe), e (elephant), c (chick), and h (hen).

The third and fourth letters represent digits that give the coordinates of the
current position of the piece if the piece is to be moved or promoted and
represent the position that the piece will be dropped to if the piece is to be
dropped. The fifth and sixth letters represent the location that the piece will
move to if the piece is to be moved or promoted. The letters i and k denote
horizontal coordinates and the letters j and l denote vertical coordinates.

For instance, given the initial position displayed below (where we number the
ranks and files and display Player A and Player B for clarity),

Player B \n
   1    2    3 \n
1  G    L    E \n
2  *    C    * \n
3  *    c    * \n
4  e    l    g \n
Player A

Player A could input the command 'mc3222' to move his/her chick and capture
Player B's chick. The first two digits '32' represents the fact that Player
A's chick is on square (3,2) and the last two digits '22' represents the fact
that Player A's chick will move to square (2,2). This would result in the
following.

Player B \n
   1    2    3 \n
1  G    L    E \n
2  *    c    * \n
3  *    *    * \n
4  e    l    g \n
Player A (has c in hand)

If the following position is reached

Player B \n
   1    2    3 \n
1  L    *    * \n
2  *    E    C \n
3  *    e    * \n
4  C    l    g \n
Player A (has g in hand)

and if it's Player A's turn, Player A can input the command 'dg21' to drop
his/her giraffe into the square (2,1) resulting in the following.

Player B \n
   1    2    3 \n
1  L    *    * \n
2  g    E    C \n
3  *    e    * \n
4  C    l    g \n
Player A

Lastly, given the following position, and assuming that it is Player A to move,

Player B \n
   1    2    3 \n
1  *    L    G \n
2  c    E    * \n
3  G    e    c \n
4  *    *    l \n
Player A

Player A can input the command 'pc2111' to promote his/her chick, resulting in
the following.

Player B \n
   1    2    3 \n
1  h    L    G \n
2  *    E    * \n
3  G    e    c \n
4  *    *    l \n
Player A '''

    return command_instructions

# The following function translates the above commands into equivalent commands
# from the actions dictionary in board.py, then calls the perform function to
# perform the translated command. The function takes as input, which player is
# inputting the command as its first argument, the command to be translated in
# the second argument, and the board (with the pieces associated with it) that
# the command will affect as the third argument.

def translate(side, command, pieces):

    if command[0] in ('m', 'p'):
        i,j = int(command[2]), int(command[3])

        for type in pieces:
            for piece in pieces[type]:
                if piece[0] is not None and piece[1] == (i,j):
                    replica = pieces[type].index(piece)


        st = command[:2].upper() + str(replica)
        ti = int(command[4]) - int(command[2])
        tj = int(command[5]) - int(command[3])

    elif command[0] == 'd':

        for type in pieces:
            for piece in pieces[type]:
                if piece[0] == side and piece[1] is None:
                    if convert(side, type).lower() == command[1]:
                        replica = pieces[type].index(piece)

        st = command[:2].upper() + str(replica)
        ti, tj = int(command[2]), int(command[3])

    action = (st, (ti, tj))

    return action

# The following function receives commands from the player and executes those
# commands. This function has no side effects because the translate and perform
# functions have no side effects. The first argument determines the player
# inputting the command, the second argument determines the command being
# inputted by the player, and the third argument represents the board (including
# all pieces involved) that the command will affect.

def enter(side, command, pieces):
    try:
        action = translate(side, command, pieces)
    except:
        print("Press enter to exit the game.")
        input()
        quit()
    return perform(action, pieces)
