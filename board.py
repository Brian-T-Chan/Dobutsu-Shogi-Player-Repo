# Brian Chan
# March 2021

from board_hardware import perform

# This program gives a represention of the Dobutsu Shogi game board and its
# pieces. In addition to this, this program has data structures and functions
# that provide core functionality to support the game board and its associated
# pieces. This program, combined with board_hardware.py, make up the essential
# code for a functioning Dobutsu Shogi game board with its associated pieces.

# The ranks (the rows) of the Dobutsu Shogi game board are numbered 1 through 4
# from top to bottom. The files (the columns) are numbered 1 through 3 from left
# to right. Squares are denoted (i,j) where i denotes the row number of the row
# containing the square and where j denote the column number of the column
# containing the square. Player A is the player whose pieces at the beginning
# of the game are on squares (4,1), (4,2), (4,3), and (3,2). Player B is the
# other player. Below is a reference.

# Player B
#    1  2  3
# 1  G  L  E
# 2  *  C  *
# 3  *  c  *
# 4  e  l  g
# Player A

# In these programs, a and b will denote the players involved in the game.
a, b = 'A', 'B'


# The game board and the pieces involved with that game board are
# represented by a dictionary of the following form.

# pieces = {'lion' : ([ ... , ... ], [ ... , ... ]), \
#           'giraffe' : ([ ... , ... ], [ ... , ... ]), \
#           'elephant' : ([ ... , ... ], [ ... , ... ]), \
#           'chick' : ([ ... , ... ], [ ... , ... ]), \
#           'hen' :  ([ ... , ... ], [ ... , ... ]) }

# Each key of the above dictionary represents the type of the piece, and
# the value assigned to the key is a tuple representing the two pieces of
# any given type (there are two lions, two giraffes, etc). Every piece

# piece = [ ... , ... ]

# is a length two list with the following properties. If piece[0] == a, then
# piece belongs to Player A, and if piece[0] == b, then piece belongs to
# Player B. If piece[1] == (i,j), then the piece is on the board and located
# on square (i,j). If piece[0] == a and if piece[1] == None, then piece belongs
# to Player A and is in Player A's hand. Lastly, if piece[0] == b and if
# piece[1] == None, then piece belongs to Player B and is in Player B's hand.

# If piece is of the form

# piece = [None, ... ]

# (specifically, if the condition, piece[0] is None == True, is true) then
# the piece is not considered to be ''in play''. Such a distinction is made
# because the game allows for a chick to be promoted to a hen and because
# any captured hen reverts to a chick. When a chick promotes to a hen, the
# piece representing the chick is no longer in play and a piece, representing
# a hen, that was not in play is brought into play. Similarly, when a hen is
# captured, the piece representing the hen is no longer in play and a piece,
# representing a chick, that was not in play is brought back into play. A piece
# of the form [None, ...] can, be [None, None] or [None, (i,j)]. Importantly,
# if piece[0] is None, then piece[1] is irrelevant and should be ignored.

# The followinng dictionary, initialstate, represents the initial position of
# all the pieces in the Dobutsu Shogi game. For instance, initialstate['lion']
# == ([a,(4,2)], [b,(1,2)]) because at the beginning of the game Player A's lion
# is on square (4,2) and Player B's game is on square (1,2). Moreover,
# initialstate['hen'] == ([None,None], [None,None]) since there are no hens
# at the beginning of the game.

initialstate = {'lion' : ([a,(4,2)], [b,(1,2)]), \
                'giraffe' : ([a,(4,3)], [b,(1,1)]), \
                'elephant' : ([a,(4,1)], [b,(1,3)]), \
                'chick' : ([a,(3,2)], [b,(2,2)]), \
                'hen' :  ([None,None], [None,None]) }


# The actions dictionary below gives all possible commands that can be given
# to the above data structure (the game board + pieces). The commands are
# subdivided into categories according to which piece the command involves.
# The names of said categories are the keys in this dictionary. Each command is
# also referred to as an action in board_hardware.py, the program that will
# read these commands and implement them. If the command/action is not a legal
# move, then the action will be ignored by board_hardware.py and the perform
# function in board_hardware.py will return None. Each action/command is of the
# following form.

# ('ABC', (si,sj))

# where A signifies the type of command being requested, B signifies the type
# of the piece that command involves, and C signifies which piece of the
# specified type the command involves, Specifically, D, M, and P represent
# drop, move, and promote respectively, L, G, E, C, and H represent lion,
# giraffe, elephant, chick, and hen respectively, and C can be 0 or 1.

# Moreover, (si,sj) signifies the following. If A is equal to D, then (si,sj),
# signifies which square the piece should be dropped to. If A is equal to M
# or equal to P, then (si,sj) signifies the change in location requested for
# the piece being moved. Specifically, if the piece on the board to be moved
# or promoted in on square (i,j), then the action/command requests the piece
# to be moved to square (i + si, j + sj).

# Example: Let piece be the dictionary
# described above. The action

# ('DG1', (2,3))

# asks the program to drop the giraffe represented by piece['giraffe'][1] onto
# the square (2,3). The action

# ('ME0', (1,-1))

# asks the program to move the elephant represented by piece['elephant'][0]
# one row lower and one column to the left (if such a move is a legal move,
# and if an opponent's piece is in the way, then that piece will be captured).

# The action

# ('PC1', (0,-1))

# asks to program to promote the chick represented by the piece['chick'][1]
# by asking it to move one row up and to have it promote to a hen (such a
# promotion will remove the piece piece['chick'][1] from play and will put a
# piece of the form piece['hen'][s] into play).

board = []

for i in [1,2,3,4]:
    for j in [1,2,3]:
        board.append((i,j))

actions = {
'DG0' : [('DG0', (i,j)) for i,j in board],
'DG1' : [('DG1', (i,j)) for i,j in board],
'DE0' : [('DE0', (i,j)) for i,j in board],
'DE1' : [('DE1', (i,j)) for i,j in board],
'DC0' : [('DC0', (i,j)) for i,j in board],
'DC1' : [('DC1', (i,j)) for i,j in board],
'ML0' : [('ML0', (i,j)) for i,j in [(-1,-1), (-1,0), (-1,1), (0,-1),\
                                       (0,1), (1,-1), (1,0), (1,1)]],
'ML1' : [('ML1', (i,j)) for i,j in [(-1,-1), (-1,0), (-1,1), (0,-1),\
                                      (0,1), (1,-1), (1,0), (1,1)]],
'MG0' : [('MG0', (i,j)) for i,j in [(-1,0), (0,-1), (0,1), (1,0)]],
'MG1' : [('MG1', (i,j)) for i,j in [(-1,0), (0,-1), (0,1), (1,0)]],
'ME0' : [('ME0', (i,j)) for i,j in [(-1,-1), (-1,1), (1,-1), (1,1)]],
'ME1' : [('ME1', (i,j)) for i,j in [(-1,-1), (-1,1), (1,-1), (1,1)]],
'MC0' : [('MC0', (-1,0)), ('MC0', (1,0))],
'PC0' : [('PC0', (-1,0)), ('PC0', (1,0))],
'MC1' : [('MC1', (-1,0)), ('MC1', (1,0))],
'PC1' : [('PC1', (-1,0)), ('PC1', (1,0))],
'MH0' : [('MH0', (i,j)) for i,j in [(-1,-1), (-1,0), (-1,1), (0,-1),\
                                               (0,1), (1,-1), (1,0), (1,1)]],
'MH1' : [('MH1', (i,j)) for i,j in [(-1,1), (-1,0), (-1,-1), (0,-1),\
                                               (0,1), (1,-1), (1,0), (1,1) ]]
}


# Returns a list of the aforementioned commands/actions. The list consists of
# actions that would act on a player (determined by the first parameter of this
# function) and that would involve pieces currently in that player's possesion
# given the current state of the game (determined by the third parameter of this
# function). This function may also return commands that are impossible to
# perform on the board; i.e., the return value of this function may contain
# a member, action, such that perform(action, pieces) returns None.

def selection(side, pieces):

    inventory = {}

    for type in pieces:
        for piece in pieces[type]:
            if piece[0] == side:
                replica = pieces[type].index(piece)
                replica = str(replica)
                if type == 'lion':
                    if piece[1] is None:
                        key = 'DL' + replica
                    else:
                        key = 'ML' + replica
                elif type == 'giraffe':
                    if piece[1] is None:
                        key = 'DG' + replica
                    else:
                        key = 'MG' + replica
                elif type == 'elephant':
                    if piece[1] is None:
                        key = 'DE' + replica
                    else:
                        key = 'ME' + replica
                elif type == 'chick':
                    if piece[1] is None:
                        key = 'DC' + replica
                    elif side == a and piece[1][0] == 2:
                        key = 'PC' + replica
                    elif side == b and piece[1][0] == 3:
                        key = 'PC' + replica
                    else:
                        key = 'MC' + replica
                elif type == 'hen':
                    if piece[1] is None:
                        key = 'DH' + replica
                    else:
                        key = 'MH' + replica
                inventory[key] = None

    selection = []
    for key in inventory:
        selection = selection + actions[key]
    return selection

# The two functions below determine which side, if any, has won the game given
# the current positions of all of the pieces (represented by the parameter,
# pieces, in both of the below functions). Return value is 'A' (as a == 'A')
# if Player A has won and 'B' (as b = 'B') if Player B has won. Returns None
# if neither player has won. These functions heavily depend on the initialstate
# dictionary to function properly. Moreover, these functions allow for the
# situations where both players have won and lost (if both players have
# captured each other lions, for example) and they will return 'A' or 'B' but
#  not both. These functions should not be used for such situations.

# The capturewin function determines if a player has won by capturing his/her
# opponent's lion. The 'checkmate' notion is not implemented in this function.

# The noncapturewin function determines if a player has won or lost by moving
# his/her lion into the furthest rank. However, if the lion is already captured,
# then this function gives the same return value as the capturewin function.
# In these comments, the term ''furthest rank'' is a relative term. If Player A
# has a piece on the furthest rank, that piece is on Rank 1, and if Player B
# has a piece on the furthest rank, that piece is on Rank 4.

def capturewin(pieces):

    # If Player B's lion is captured.
    if pieces['lion'][1][0] == a:
        return a

    # If Player A's lion is captured.
    if pieces['lion'][0][0] == b:
        return b

def noncapturewin(pieces):

    # If a lion is already captured, then this function reverts to being
    # the capturewin function.

    lioncapture = capturewin(pieces)
    if lioncapture is not None : return lioncapture

    # If Player A's lion has reached the furthest rank.

    if pieces['lion'][0][1][0] == 1:
        selectedactions = selection(b, pieces)
        for action in selectedactions:
            state = perform(action, pieces)
            if state is not None:
                if capturewin(state) == b:
                    return b
        return a

    # If Player B's lion has reached the furthest rank.

    if pieces['lion'][1][1][0] == 4:
        selectedactions = selection(a, pieces)
        for action in selectedactions:
            state = perform(action, pieces)
            if state is not None:
                if capturewin(state) == a:
                    return a
        return b


# This function determines which player has at least two more pieces than
# his/her opponent. Returns 'A' if Player A has at least two more pieces,
# returns 'B' if Player B has at least two more pieces, and returns None
# otherwise.

def piecemajority(pieces):
    acount, bcount = 0, 0

    # Counts the number of pieces in Player A's possesion and in
    # Player B's possesion.
    for type in pieces:
        for piece in pieces[type]:
            if piece[0] == a : acount = acount + 1
            elif piece[0] == b : bcount = bcount + 1

    if acount >= bcount + 2 : return a
    elif bcount >= acount + 2 : return b
