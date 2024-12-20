def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def take_input(player, board):
    valid = False
    while not valid:
        player_move = input(f"Player {player}, enter your move (row, col): ")
        try:
            row, col = map(int, player_move.split(','))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                valid = True
                board[row][col] = player
            else:
                print("Invalid move. Try again.")
        except:
            print("Please enter two numbers separated by a comma.")
    print_board(board)

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def check_tie(board):
    return all(board[row][col] != " " for row in range(3) for col in range(3))


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print_board(board)
    players = ['X', 'O']
    turn = 0

    while True:
        take_input(players[turn], board)
        if check_win(board, players[turn]):
            print(f"Player {players[turn]} wins!")
            break
        if check_tie(board):
            print("It's a tie!")
            break
        turn = 1 -turn

tic_tac_toe()

