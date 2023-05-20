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

def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE if piece == AI_PIECE else AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score

def score_position(board, piece):
    # Score center column
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
    center_count = center_array.count(piece)
    score = center_count * 3

    # Score horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLUMN_COUNT-WINDOW_LENGTH+1):
            window = row_array[c:c+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Score vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(ROW_COUNT-WINDOW_LENGTH+1):
            window = col_array[r:r+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # Score positive diagonal
    for r in range(ROW_COUNT-WINDOW_LENGTH+1):
        for c in range(COLUMN_COUNT-WINDOW_LENGTH+1):
            window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    # Score negative diagonal
    for r in range(ROW_COUNT-WINDOW_LENGTH+1):
        for c in range(COLUMN_COUNT-WINDOW_LENGTH+1):
            window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score

def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations

def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)

    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -100000000000000)
            else: # Game is over, no more valid moves
                return (None, 0)
        else: # Depth is zero
            return (None, score_position(board, AI_PIECE))

    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = copy.deepcopy(board)
            drop_piece(temp_board, row, col, AI_PIECE)
            new_score = minimax(temp_board, depth-1, alpha, beta, False)[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value
    else: # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            temp_board = copy.deepcopy(board)
            drop_piece(temp_board, row, col, PLAYER_PIECE)
            new_score = minimax(temp_board, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value
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

def Computer_Play(board,ROWS,COLS):
    if Priority_ONE(board,6,7)!=-1:
        Col = Priority_ONE(board, 6, 7)
        return Col
    elif Priority_TWO(board,6,7) !=-1:
        Col = Priority_TWO(board,6,7)
        return Col
    elif Priority_THREE(board,6,7) !=-1:
        Col = Priority_THREE(board,6,7)
        return Col
    else:
        return 3
    print("--------------------------------------------")

def play_game():
    board = create_board()
    turn = PLAYER

    while not is_terminal_node(board):
        if turn == PLAYER:
            col = Computer_Play(board,ROW_COUNT,COLUMN_COUNT)
            print("Computer's turn...")
            print(f"Computer chose column: {col}")
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, PLAYER_PIECE)
                if winning_move(board, PLAYER_PIECE):
                    print("Agent wins!")
                    return
            else:
                print("Invalid Move. Try again.")
                continue
        else:
            col, minimax_score = minimax(board, 4, -math.inf, math.inf, True)
            print("AI Agent's turn...")
            print(f"AI Agent chose column: {col}")
            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, AI_PIECE)
                if winning_move(board, AI_PIECE):
                    print("AI wins!")
                    return
            else:
                print("Invalid Move. Try again.")
                continue

        print_board(board)
        turn = (turn + 1) % 2

    print("It's a tie!")

play_game()