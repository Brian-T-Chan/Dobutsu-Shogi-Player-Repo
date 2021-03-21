# Brian Chan
# March 2021

# Constants indicating the players involved.
a, b = 'A', 'B'

# The following program displays the Dobutsu Shogi game board along with the
# locations of all the pieces in the board and in the player's hands. 

# Specifically, the program converts the data structure in board.py that
# represents the game board and the pieces into a visual display. The pieces
# are maked with upper or lower-case letters. Which letters are being used
# indicate the type of piece and whether the letter is upper or lower-
# case determines which side the piece belongs to. Specifically,
#
# l, L : lion
# g, G : giraffe
# e, E : elephant
# c, C : chick
# h, H : hen
#
# A lower case letter represents a piece under Player A's control and an
# upper case letter represents a piece under Player B's control. The initial
# position of the game is displayed by this program in the following way
# (not to scale).

# -------------
# -------------
#    1   2   3
# 1  G   L   E
# 2  *   C   *
# 3  *   c   *
# 4  e   l   g
# -------------
# -------------

# Pieces captured by Player A will appear in the lower bar and pieces captured
# by Player B will appear in the upper bar.

# Give a visual representation of a board piece.

def convert(side, type):

    if side == a and type == 'lion':
        return 'l'
    elif side == b and type == 'lion':
        return 'L'
    elif side == a and type == 'giraffe':
        return 'g'
    elif side == b and type == 'giraffe':
        return 'G'
    elif side == a and type == 'elephant':
        return 'e'
    elif side == b and type == 'elephant':
        return 'E'
    elif side == a and type == 'chick':
        return 'c'
    elif side == b and type == 'chick':
        return 'C'
    elif side == a and type == 'hen':
        return 'h'
    elif side == b and type == 'hen':
        return 'H'

# Visually represent the current state of the game board by displaying the
# board, the pieces on the board, and the pieces in each of the player's
# hands. Only pieces currently in play are displayed.

def display(pieces):

    if pieces is None:
        print('Invalid Input.')
        return

    board = []

    for i in [1,2,3,4]:
        board.append([])
        for j in [1,2,3]:
            board[i-1].append('  *  ')

    ahand = {}
    bhand = {}

    # Visually represent the pieces on the board. Moreover, record the pieces
    # that are in each player's hand.
    for type in pieces:
        for piece in pieces[type]:
            if piece[0] is not None and piece[1] is not None:
                i,j = piece[1]
                symbol = convert(piece[0], type)
                board[i-1][j-1] = '  ' + symbol + '  '

            elif piece[0] is not None and piece[1] is None:
                if piece[0] == a:
                    ahand[type] = ahand.get(type, 0) + 1
                if piece[0] == b:
                    bhand[type] = bhand.get(type, 0) + 1

    aorder = sorted(ahand)
    border = sorted(bhand)

    # Print the pieces in Player B's hand and print the column numbers.
    print()
    print('---------------')
    for type in border:
        for i in range(bhand[type]):
            symbol = convert(b, type)
            print(symbol + ' ', end = '')
    print()
    print('---------------')
    print('    1    2    3')
    print()

    # Print the board and all pieces on it. In addition, print the row numbers.
    for i in range(4):
        print(str(i + 1) + ' ', end = '')
        for j in range(3):
            print(board[i][j], end = '')
        print()
        if i < 3:
            print()

    # Print the pieces in Player A's hand.
    print('---------------')
    for type in aorder:
        for i in range(ahand[type]):
            symbol = convert(a, type)
            print(symbol + ' ', end = '')
    print()
    print('---------------')
