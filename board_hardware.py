# Brian Chan
# March 2021

from copy import deepcopy

# Constants indicating the players involved.
a, b = 'A', 'B'

# The following program implements the action of moving or dropping a piece
# on the Dobutsu Shogi board. Combined with board.py, these two progrms make
# up the essential code for a functioning Dobutsu Shogi board with its
# associated pieces.

# Player B
#    1  2  3
# 1  G  L  E
# 2  *  C  *
# 3  *  c  *
# 4  e  l  g
# Player A

# Perform an action from the actions dictionary in board.py to the board. The
# first parameter represents the requested action and the second parameter
# represents the board (including the pieces on the board and the pieces in
# each player's hand). This function has no side effects. If the requested
# action is a legal move, then the function will return a modified board
# representing the result of the requested action that was performed. Otherwise,
# if the requested action is not a legal move, then the function returns None.

def perform(action, pieces):
    newpieces = deepcopy(pieces)

    # Determine the type of the piece being used.
    if action[0][1] == 'L' : type = 'lion'
    elif action[0][1] == 'G' : type = 'giraffe'
    elif action[0][1] == 'E' : type = 'elephant'
    elif action[0][1] == 'C' : type = 'chick'
    elif action[0][1] == 'H' : type = 'hen'

    # Determine which piece (among the two pieces of the type selected) that
    # will be used.
    replica = int(action[0][2])

    # Keep track of the selected piece.
    the_piece = newpieces[type][replica]
    # Record whose side the piece belongs to.
    playing_side = the_piece[0]
    # Determine what kind of action is to be performed with the piece.
    action_type = action[0][0]
    # Determines the drop location if the piece is being dropped and the change
    # in location otherwise.
    si, sj = action[1]

    # If the piece does not represent a piece currently in play, then abort.
    if playing_side is None : return

    # Initialize variables i and j which represent the location on the board
    # the selected piece will move towards if not in ``drop mode''.
    if action_type in ('M', 'P'):
        if the_piece[1] is None : return

        i, j = the_piece[1]
        i, j = i + si, j + sj

        if i < 1 or i > 4 or j < 1 or j > 3:
            return

    # Ensure that a piece is promoted only if the chick has reached the
    # furthest rank.
    if action_type == 'P':
        if playing_side == a and i > 1 : return
        if playing_side == b and i < 4 : return

    # Ensure that a move is made only if it is not a chick moving to the
    # furthest rank (such an action has to be a promotion).
    if action_type == 'M' and type == 'chick':
        if playing_side == a and i == 1 : return
        if playing_side == b and i == 4 : return

    # Ensure that, if the chick or hen is used, that a legal move is being made
    # on the board.
    if action_type in ('M', 'P') and type == 'chick':
        if playing_side == a and si == 1 : return
        if playing_side == b and si == -1 : return

    elif action_type in ('M', 'P') and type == 'hen':
        if playing_side == a:
            if (si,sj) == (1,-1) or (si,sj) == (1,1):
                return
        if playing_side == b:
            if (si,sj) == (-1,-1) or (si,sj) == (-1,1):
                return

    # Perform a drop action.
    if action_type == 'D' and the_piece[1] is None:
        # Abort if there is another piece on the board that is in the way.
        for kind in newpieces:
            for piece in newpieces[kind]:
                if piece[1] == (si,sj) : return

        # Drop the piece.
        the_piece[1] = (si,sj)

    # Perform a move or promote action.
    elif action_type in ('M', 'P'):
        # Determine the piece that is being captured, if any.
        captured = None
        captured_type = None

        for kind in newpieces:
            for piece in newpieces[kind]:
                if piece[0] is not None and piece[1] == (i,j):
                    captured = piece
                    captured_type = kind

        # If a piece is captured, do the following.
        if captured is not None:
            # Ensures that a player does not capture his/her piece by aborting
            # if necessary.
            if captured[0] == playing_side : return

            # If a hen is captured, remove the hen from current play. Next,
            # bring a chick that is not in play back into play, and keep it
            # in the hand of the player who made the capture.
            elif captured_type == 'hen':
                captured[0] = None
                removed = []

                for piece in newpieces['chick']:
                    if piece[0] is None:
                        removed.append(piece)

                captured_chick = removed[0]

                captured_chick[0] = playing_side
                captured_chick[1] = None


            # If a non-hen piece is captured, then have the player collect
            # the piece and place it into his/her hand.
            else:
                captured[0] = playing_side
                captured[1] = None

        # Move the selected piece the_piece on the board if the piece is not
        # a chick being promoted.
        if action_type == 'M' : the_piece[1] = (i,j)

        # Remove the selected piece, the chick about to be promoted, from play.
        # Next, take a hen not in play and put it into play be placing it on
        # the board in the position (i,j).
        elif action_type == 'P':
            the_piece[0] = None
            removed = []
            for piece in newpieces['hen']:
                if piece[0] is None:
                    removed.append(piece)
            promoted = removed[0]
            promoted[0] = playing_side
            promoted[1] = (i,j)

    # Cannot drop a piece that is already on the board.
    else : return

    # Return the modified board.
    return newpieces
