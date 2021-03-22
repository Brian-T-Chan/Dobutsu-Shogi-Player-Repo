# Brian Chan
# March 2021

# The following program uses alpha-beta pruning to evaluate a given position
# in the Dobutsu Shogi game. To ensure that the program does not always give
# the same replies to moves (when more than one game is played), the children
# of the root node of the search tree of this algorithm are randomly permuted
# before the beginning of alpha-beta pruning. During the execution of alpha-
# beta pruning, the order of the children of the root node (determined before
# the start of alpha-beta pruning) is fixed.

# The program always assumes the role of Player B
# and is the maximizing player (player who wants to maximize his/her alpha
# score) in the below program. The minimizing player (player who wants to
# minimize his/her beta score) is always Player A. The evaluation function is
# scored as follows.

# Player A wins (in a way specified by the capturewin and noncapture win
# functions in board.py) : -1
# Player B wins (in a way specified by the capturewin and noncapture win
# functions in board.py) : 1

# In addition to using the alpha-beta pruning algorithm, the following is
# done to skew scores when not at the root node (root node of the search tree
# for alpha beta pruning).

# If neither Player A nor Player B is considered to have won, then add
# 0.01 to the score if Player B has at least two more pieces than Player A
# and subtract 0.01 from the score in Player A has at least two more pieces
# than Player A.

# So for instance, if the search depth is set to 6 and if a candidate move for
# Player B is a sure win within six moves for Player B but involves Player B
# having at least two fewer pieces than Player A for the rest of the game, then
# the score for that candidate move would be at least: 1 - 5 * 0.01 = 0.95.

# The ideal search depth for this program would be between 3 and 7 inclusive.

import math
import random

from board import capturewin, noncapturewin, selection, piecemajority
from board_hardware import perform

# Player B
#    1  2  3
# 1  G  L  E
# 2  *  C  *
# 3  *  c  *
# 4  e  l  g
# Player A

# Constants indicating the players involved.
a, b = 'A', 'B'

# There are three functions below that run this program. alphabeta returns an
# optimal move (move = moving a piece or dropping a piece) whereas maximizer
# and minimizer return integers representing scores. alphabeta is used to
# perform alpha-beta pruning at the root node of the search tree. maximizer
# and minimizer are run when performing alpha-beta pruning at the other nodes.

# Don't directly call maximizer or minimizer, call alphabeta. Maximizer and
# minimizer recursively call each other and run when alphabeta is called.
# alphabeta has additional code for randomizing optimal moves. In alphabeta,
# the randomization is performed in such a way that the alpha-beta pruning
# algorithm is not compromised.

# This function represents the maximizing player, Player B, in the modified
# alpha-beta pruning algorithm (alpha-beta pruning + skewing scores as
# described above).

def maximizer(pieces, depth, alpha, beta):

    # Skew the score if one side has at least two more pieces.
    skew = 0
    majority = piecemajority(pieces)
    if majority == a : skew = -0.01
    elif majority == b : skew = 0.01

    # If one side wins, provide a score. Otherwise, if the depth
    # limit has been reached, provide the score skew.
    if capturewin(pieces) == b : return 1
    elif noncapturewin(pieces) == b : return 1
    elif capturewin(pieces) == a : return -1
    elif noncapturewin(pieces) == a : return -1
    elif depth == 0 : return skew

    # Determine all candidate moves for Player B at this node.
    selected = selection(b, pieces)
    possibilities = []

    for action in selected:
        possibilities.append(perform(action, pieces))

    possibilities = [i for i in possibilities if i is not None]

    # Apply alpha-beta pruning to this node.
    maximinlist = []

    for possibility in possibilities:
        value = minimizer(possibility, depth - 1, alpha, beta)
        maximinlist.append(value)
        alpha = max(alpha, value)
        if beta <= alpha:
            break

    return max(maximinlist) + skew

# This function represents the minimizing player, Player A, in the modified
# alpha-beta pruning algorithm (alpha-beta pruning + skewing scores as
# described above).

def minimizer(pieces, depth, alpha, beta):

    # Skew the score if one side has at least two more pieces.
    skew = 0
    majority = piecemajority(pieces)
    if majority == a : skew = -0.01
    elif majority == b : skew = 0.01

    # If one side wins, provide a score. Otherwise, if the depth
    # limit has been reached, provide the score skew.
    if capturewin(pieces) == a : return -1
    elif noncapturewin(pieces) == a : return -1
    elif capturewin(pieces) == b : return 1
    elif noncapturewin(pieces) == b : return 1
    elif depth == 0 : return skew

    # Determine all candidate moves for Player A at this node.
    selected = selection(a, pieces)
    possibilities = []

    for action in selected:
        possibilities.append(perform(action, pieces))

    possibilities = [i for i in possibilities if i is not None]

    # Apply alpha-beta pruning to this node.
    minimaxlist = []

    for possibility in possibilities:
        value = maximizer(possibility, depth - 1, alpha, beta)
        minimaxlist.append(value)
        beta = min(beta, value)
        if beta <= alpha:
            break

    return min(minimaxlist) + skew

# Call this function when running the modified alpha-beta pruning algorithm
# (alpha-beta pruning + skewing scores as described above + move randomization).
# Depth should be at least 1. The data structure this function returns is the
# data structure described in board.py that represents the game board and the
# pieces.

def alphabeta(pieces, depth, alpha = -math.inf, beta = +math.inf):

    if depth <= 0 : return

    selected = selection(b, pieces)
    # Randomly permute the children of the root node before alpha-beta
    # pruning begins.
    random.shuffle(selected)
    possibilities = []

    # Determine all candidate moves for Player B.
    for action in selected:
        possibilities.append(perform(action, pieces))

    possibilities = [i for i in possibilities if i is not None]

    # Apply alpha-beta pruning to the root node.
    maximinlist = []

    for possibility in possibilities:
        value = minimizer(possibility, depth - 1, alpha, beta)
        maximinlist.append(value)
        alpha = max(alpha, value)

    maxvalue = max(maximinlist)
    maxindex = maximinlist.index(maxvalue)

    return possibilities[maxindex]
