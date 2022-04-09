import copy
import random
from copy import deepcopy
import math
import State
import numpy as np
import Cell


def check_Adjancy_Limit(state: State):
    # check rows
    for i in range(0, state.size):
        for j in range(0, state.size - 2):
            if (state.board[i][j].value.upper() == state.board[i][j + 1].value.upper() and
                    state.board[i][j + 1].value.upper() == state.board[i][j + 2].value.upper() and
                    state.board[i][j].value != '_' and
                    state.board[i][j + 1].value != '_' and
                    state.board[i][j + 2].value != '_'):
                return False
    # check cols
    for j in range(0, state.size):  # cols
        for i in range(0, state.size - 2):  # rows
            if (state.board[i][j].value.upper() == state.board[i + 1][j].value.upper()
                    and state.board[i + 1][j].value.upper() == state.board[i + 2][j].value.upper()
                    and state.board[i][j].value != '_'
                    and state.board[i + 1][j].value != '_'
                    and state.board[i + 2][j].value != '_'):
                return False

    return True


def check_circles_limit(state: State):  # returns false if number of white or black circles exceeds board_size/2
    # check in rows
    for i in range(0, state.size):  # rows
        no_white_row = 0
        no_black_row = 0
        for j in range(0, state.size):  # each col
            # if cell is black or white and it is not empty (!= '__')
            if state.board[i][j].value.upper() == 'W' and state.board[i][j].value != '_': no_white_row += 1
            if state.board[i][j].value.upper() == 'B' and state.board[i][j].value != '_': no_black_row += 1
        if no_white_row > state.size / 2 or no_black_row > state.size / 2:
            return False
        no_black_row = 0
        no_white_row = 0

    # check in cols
    for j in range(0, state.size):  # cols
        no_white_col = 0
        no_black_col = 0
        for i in range(0, state.size):  # each row
            # if cell is black or white and it is not empty (!= '__')
            if state.board[i][j].value.upper() == 'W' and state.board[i][j].value != '_': no_white_col += 1
            if state.board[i][j].value.upper() == 'B' and state.board[i][j].value != '_': no_black_col += 1
        if no_white_col > state.size / 2 or no_black_col > state.size / 2:
            return False
        no_black_col = 0
        no_white_col = 0

    return True


def is_unique(state: State):  # checks if all rows are unique && checks if all cols are unique
    # check rows1
    for i in range(0, state.size - 1):
        for j in range(i + 1, state.size):
            count = 0
            for k in range(0, state.size):
                if (state.board[i][k].value.upper() == state.board[j][k].value.upper()
                        and state.board[i][k].value != '_'
                        and state.board[j][k].value != '_'):
                    count += 1
            if count == state.size:
                return False
            count = 0

    # check cols
    for j in range(0, state.size - 1):
        for k in range(j + 1, state.size):
            count_col = 0
            for i in range(0, state.size):
                if (state.board[i][j].value.upper() == state.board[i][k].value.upper()
                        and state.board[i][j].value != '_'
                        and state.board[i][k].value != '_'):
                    count_col += 1
            if count_col == state.size:
                return False
            count_col = 0

    return True


def is_assignment_complete(state: State):  # check if all variables are assigned or not
    for i in range(0, state.size):
        for j in range(0, state.size):
            if (state.board[i][j].value == '_'):  # exists a variable wich is not assigned (empty '_')

                return False

    return True


def LCV_HEURISTIC(state: State):
    pass


def FORWARD_CHECKING(state: State):
    pass


def check_constraints(state: State):
    if check_Adjancy_Limit(state) and check_circles_limit(state) and is_unique(state):
        return True


"""

"""


def MRV_HEURISTIC(state: State):
    # print(state.board)
    for row in state.board:
        for i in range(len(row)):
            if i < 2:
                if i == 0:
                    if row[i + 1].value != '_' and (row[i + 1].value == row[i + 2].value):
                        row[i].value = row[i+1].value.lower()
                        row[i].change_color()
                if i == 1:
                    if row[i + 1].value != '_' and (
                            row[i - 1].value == row[i + 1].value or row[i + 1].value == row[i + 2].value):
                        row[i].value = row[i + 1].value.lower()
                        row[i].change_color()
            elif i > state.size - 3:
                if i == state.size - 2:
                    if row[i - 1].value != '_' and \
                            (row[i - 1].value == row[i + 1].value or row[i - 1].value == row[i - 2].value):
                        print(row[i - 1].value, row[i - 2].value, row[i + 1].value)
                        row[i].value = row[i + 1].value.lower()
                        row[i].change_color()
                if i == state.size - 1:
                    if row[i - 1].value != '_' and (row[i - 1].value == row[i - 2].value):
                        row[i].value = row[i + 1].value.lower()
                        row[i].change_color()
            else:
                if row[i + 1].value != '_' and \
                        (row[i + 1].value == row[i + 2].value or row[i - 1].value == row[i + 1].value):
                    row[i].value = row[i + 1].value.lower()
                    row[i].change_color()
                    # print(row[i].x, row[i].y)
                    # print(row[i].domain)
                    # print(row[i + 1].value)
                elif row[i - 1].value != '_' and (row[i - 1].value == row[i - 2].value):
                    row[i].value = row[i + 1].value.lower()
                    row[i].change_color()
    board = state.board
    # reverseBoard = np.array(state.board).T.tolist()
    # state.board = reverseBoard
    # print("reverse board")
    # state.print_board()


def backtracking_search(firstState):
    queue = []
    stack = [firstState]
    while True:
        state = stack.pop(-1)
        if is_assignment_complete(state):
            state.print_board()
            return
        queue = []
        for row in state.board:
            for cell in row:
                if cell.value == '_':
                    queue.append(cell)
        cell = queue.pop(0)
        for value in cell.domain:
            cell.value = value
            if check_constraints(state):
                newState = copy.deepcopy(state)
                stack.append(newState)
                goBack = False


def is_consistent(state: State):
    return check_Adjancy_Limit(state) and check_circles_limit(state) and is_unique(state)


def check_termination(state: State):
    return is_consistent(state) and is_assignment_complete(state)
