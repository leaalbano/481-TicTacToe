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
    x_cells, o_cells = 0, 0

    rows = len(board)
    cols = len(board[0])

    # Loop through each cell of the board
    # and count each X and O cell
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == X:
                x_cells += 1
            if board[row][col] == O:
                o_cells += 1

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
        # Invalid action was passed in
        raise Exception(f'{action} is not a valid action.')

    row, col = action

    # Create a deep copy of original board
    # to leave original unmodified
    copy_of_board = copy.deepcopy(board)

    # Check whose move it is,
    # assign to row, col cell of board
    copy_of_board[row][col] = player(board)

    return copy_of_board


def check_rows(board):
    rows = len(board)
    for row in range(rows):
        if board[row][0] == board[row][1] == board[row][2]:
            # Automatically, we know all are the same. So if one is EMPTY
            # all columns in the row are EMPTY. So this is why this works.
            if board[row][0] != EMPTY:
                return board[row][0]

    return False


def check_cols(board):
    cols = len(board)
    for col in range(cols):
        if board[0][col] == board[1][col] == board[2][col]:
            # Automatically, we know all are the same. So if one is EMPTY
            # all cells in the column are EMPTY. So this is why this works.
            if board[0][col] != EMPTY:
                return board[0][col]

    return False


def check_diagonals(board):
    # Once again, we know if there is a diagonal member
    # then the diagonal will either be all X or all Y

    # Thus, we can safely check if the first one we check
    # (board[0][0] or board[2][0]) is not EMPTY and be
    # assured all else in the current diagonal != empty
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] != EMPTY:
            return board[0][0]
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] != EMPTY:
            return board[2][0]

    return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Each should return the winner, or False if no winner
    horizontal_winner = check_rows(board)
    if horizontal_winner:
        return horizontal_winner

    vertical_winner = check_cols(board)
    if vertical_winner:
        return vertical_winner

    diagonal_winner = check_diagonals(board)
    if diagonal_winner:
        return diagonal_winner

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # checking if there is a winner
    if winner(board) != None:
        return True

    # checking if there are any empty cells; if so, return false - game still in progress
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                return False

     # if there are no more empty cells; theres a tie and game's over
    return True


def score(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    winner = winner(board)

    if winner == X:
        return 1
    elif winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    """
    psuedocode:

    def max_function(state):
        score = max(score, min_function(results(state, actions)))
        return score
		
	def min_function(state):
        return score

    """

    raise NotImplementedError
