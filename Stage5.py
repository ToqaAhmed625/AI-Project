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