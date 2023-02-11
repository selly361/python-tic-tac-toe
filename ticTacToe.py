board = [["", "", ""],
         ["", "", ""],
         ["", "", ""]
         ]


def display_board():
    for row in board:
        print(row)


def get_player_move(player):
    row = int(input("Enter row for {}'s move: ".format(player)))
    col = int(input("Enter column for {}'s move: ".format(player)))
    return (row, col)


def check_valid_move(move):
    row, col = move
    return bool(board[row][col])


def update_board(move, player):
    row, col = move
    new_board = board
    new_board[row][col] = player
    return new_board


def check_win(player):

    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True


def check_draw():
    for row in board:
        if "" in row:
            return False


def check_valid_move(move):
    row, col = move
    try:
        cell = board[row][col]
        return cell == ''
    except:
        return False


current_player = "x"

while True:
    display_board()
    move = get_player_move(current_player)

    while not check_valid_move(move):
        print("Invalid move. Please try again.")
        move = get_player_move(current_player)

    board = update_board(move, current_player)
    current_player = "X" if current_player == "x" else "O"

    if check_win(current_player):
        print("Player {} Has Won!".format(current_player))
        display_board()
        break

    elif check_draw():
        print("Draw!")
        display_board()
        break
