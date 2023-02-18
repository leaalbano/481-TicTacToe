"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_cells, o_cells, empty_cells = 0, 0, 0

    for row in board:
        # Count EACH X, 0, EMPTY cell in board
        x_cells += row.count(X)
        o_cells += row.count(O)
        empty_cells += row.count(EMPTY)

    # O's turn if num of X cells > O cells
    # Otherwise, X's turn
    return O if x_cells > o_cells else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    # Check if row, col position is empty
    # If so, add it to our possible moves set
    for row in len(board):
        for col in len(board[0]):
            if board[row][col] == EMPTY:
                possible_actions.add((row, col))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    possible_actions = actions(board)
    if action not in possible_actions:
        raise Exception(f'{action} is not a valid action.')

    row, col = action

    # Create a deep copy of original board
    # to leave original unmodified
    copy_of_board = copy.deepcopy(board)

    # Check whose move it is,
    # assign to row, col cell of board
    copy_of_board[row][col] = player(board)

    return copy_of_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
