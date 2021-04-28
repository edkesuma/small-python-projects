# is the chess board valid function

def is_valid_chess_board(board):
    valid_board = True
    black_piece_count = 0
    white_piece_count = 0
    black_pawn_count = 0
    white_pawn_count = 0
    allowed_letter_array = ["a", "b", "c", "d", "e", "f", "g", "h"]
    piece_color = ["w", "b"]
    piece_classes = ["pawn", "knight", "bishop", "rook", "queen", "king"]

    # one black king and one white king
    if ("bking" not in board.values()):
        print("You need bking and wking")
        valid_board = False
    elif ("wking" not in board.values()):
        print("You need bking and wking")
        valid_board = False

    for key, value in board.items():
        # must be in valid space within 1a to 8h
        if (int(key[0]) > 8):
            print("Number can only be between 1 to 8")
            valid_board = False
        if (key[1] not in allowed_letter_array):
            print("Letters can only be from a to h")
            valid_board = False

        # each player has max 16 pieces
        if (value != ""):
            if (value[0] == "b"):
                black_piece_count += 1
            if (black_piece_count > 16):
                print("Too many black pieces")
                valid_board = False
            if (value[0] == "w"):
                white_piece_count += 1
            if (white_piece_count > 16):
                print("Too many white pieces")
                valid_board = False

            # at most 8 pawns each
            if (value == "bpawn"):
                black_pawn_count += 1
            if (black_pawn_count > 8):
                print("Too many black pawns")
                valid_board = False
            if (value == "wpawn"):
                white_pawn_count += 1
            if (white_pawn_count > 8):
                print("Too many white pawns")
                valid_board = False

            # piece names begin with w or b
            if (value[0] not in piece_color):
                print("Piece must start with either w or b")
                valid_board = False

            # names followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'
            if (value[1:] not in piece_classes):
                print("Piece must be 'pawn', 'knight', 'bishop', 'rook', 'queen' or 'king'")
                valid_board = False
    return(valid_board)

chess_board = {'1a': 'bking','2a': 'bqueen','3a': 'brook','4a': 'brook',
'5a': 'bknight','6a': 'bknight','7a':'bbishop','8a': 'bbishop',
'1b': 'bpawn','2b': 'bpawn','3b': 'bpawn','4b':'bpawn',
'5b': 'bpawn','6b': 'bpawn','7b': 'bpawn','8b': 'bpawn',
'1c': 'wking','2c': 'wqueen','3c': 'wrook','4c': 'wrook',
'5c': 'wbishop','6c': 'wbishop','7c': 'wknight','8c':'wknight',
'1e': 'wpawn','2e': 'wpawn','3e': 'wpawn','4e': 'wpawn',
'5e': 'wpawn','6e': 'wpawn','7e': 'wpawn','8e': 'wpawn',
'1f': '','2f': '','3f': '','4f': '','5f': '','6f': '','7f': '','8f': '',
'1g': '','2g': '','3g': '','4g': '','5g': '','6g': '','7g': '','8g': '',
'1h': '','2h': '','3h': '','4h': '','5h': '','6h': '','7h': '','8h': '',}


print(str(is_valid_chess_board(chess_board)))
