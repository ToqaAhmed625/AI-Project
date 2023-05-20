import math
import copy
import random
import numpy as np

def IsAvailble(board,row,column):
    return board[row][column]== EMPTY
def Priority_ONE(board,ROWS,COLS):
    """
    Check if the specified player Close to winning Returns the state number if NOT returns 0.
    Takes the specified player token

    $  $  $  []
    """
    # horizontal                           board[row][col+3] == token
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == AI_PIECE and board[row][col+1] == AI_PIECE and board[row][col+2] == AI_PIECE and IsAvailble(board, row,col+3):
                return col+3
    # vertical                             board[row+3][col] == token
    for row in range(ROWS - 3):
        for col in range(COLS):
            if board[row][col] == AI_PIECE and board[row+1][col] == AI_PIECE and board[row+2][col] == AI_PIECE and IsAvailble(board, row+3, col):
                return col

    #diagonal (top-left to bottom-right)   board[row+3][col+3] == token
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == AI_PIECE and board[row+1][col+1] == AI_PIECE and board[row+2][col+2] == AI_PIECE and IsAvailble(board, row+3, col+3):
                return col+3

    # diagonal (bottom-left to top-right)  board[row-3][col+3] == token
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == AI_PIECE and board[row-1][col+1] == AI_PIECE and board[row-2][col+2] == AI_PIECE and IsAvailble(board, row-3, col + 3):
                return col + 3
    return -1
def Priority_TWO(board,ROWS,COLS):
    """
    $  $  []
    """
    # horizontal                           board[row][col+2] == token
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == AI_PIECE and board[row][col+1] == AI_PIECE and IsAvailble(board, row,col+2):
                return col+2

    # vertical                             board[row+2][col] == token
    for row in range(ROWS - 3):
        for col in range(COLS):
            if board[row][col] == AI_PIECE and board[row+1][col] == AI_PIECE and IsAvailble(board, row+2, col):
                return col

    #diagonal (top-left to bottom-right)   board[row+2][col+2] == token
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == AI_PIECE and board[row+1][col+1] == AI_PIECE and IsAvailble(board, row+2, col+2):
                return col+2

    # diagonal (bottom-left to top-right)  board[row-2][col+2] == token
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == AI_PIECE and board[row-1][col+1] == AI_PIECE  and IsAvailble(board, row-2, col + 2):
                return col+2
    return -1
def Priority_THREE(board,ROWS,COLS):
    """
    $  []
    """
    # horizontal                           board[row][col+1] == token
    for row in range(ROWS):
        for col in range(COLS - 3):
            if board[row][col] == AI_PIECE  and IsAvailble(board, row,col+1):
                return col+1

    # vertical                             board[row+1][col] == token
    for row in range(ROWS - 3):
        for col in range(COLS):
            if board[row][col] == AI_PIECE and IsAvailble(board, row+1, col):
                return col

    #diagonal (top-left to bottom-right)   board[row+1][col+1] == token
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if board[row][col] == AI_PIECE  and IsAvailble(board, row+1, col+1):
                return col+1

    # diagonal (bottom-left to top-right)  board[row-1][col+1] == token
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if board[row][col] == AI_PIECE  and IsAvailble(board, row-1, col + 1):
                return col+1
    return -1


