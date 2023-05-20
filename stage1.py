import math
import copy
import random
import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7
PLAYER = 0
AI = 1
EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2
WINDOW_LENGTH = 4

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == EMPTY

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == EMPTY:
            return r

def print_board(board):
    print('\n'.join([' '.join([str(board[r][c]) for c in range(COLUMN_COUNT)]) for r in reversed(range(ROW_COUNT))]))

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-WINDOW_LENGTH+1):
        for r in range(ROW_COUNT):
            if all(board[r][c+i] == piece for i in range(WINDOW_LENGTH)):
                return True

    # Check vertical location for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-WINDOW_LENGTH+1):
            if all(board[r+i][c] == piece for i in range(WINDOW_LENGTH)):
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT-WINDOW_LENGTH+1):
        for r in range(ROW_COUNT-WINDOW_LENGTH+1):
            if all(board[r+i][c+i] == piece for i in range(WINDOW_LENGTH)):
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT-WINDOW_LENGTH+1):
        for r in range(WINDOW_LENGTH-1, ROW_COUNT):
            if all(board[r-i][c+i] == piece for i in range(WINDOW_LENGTH)):
                return True

def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations

def IsAvailble(board,row,column):
    return board[row][column]== EMPTY