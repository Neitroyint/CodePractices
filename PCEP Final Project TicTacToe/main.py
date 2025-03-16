from random import randrange

def display_board(board):
    for row in board:
        print("+-------+-------+-------+\n|       |       |       |")
        for cell in row:
            print("|   " + str(cell) + "   ", end="")
        print("|")
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    try:
        input_position = int(input("Enter your move: "))
        if (input_position < 1 or input_position > 9) or input_position not in make_list_of_free_fields(board):
            print("Invalid move")
            return
        position = position_dict[input_position]
        board[position[0]][position[1]] = "O"

    except ValueError:
        print("Invalid move")
    except:
        print("There was an error")
    return board

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for row in board:
        for cell in row:
            if type(cell) is int:
                free_fields.append(cell)
    return free_fields

def victory_for(board, sign):
    # xxx, ooo, ooo
    if board[0][0] == board[0][1] == board[0][2] == sign:
        return True
    # ooo, xxx, ooo
    elif board[1][0] == board[1][1] == board[1][2] == sign:
        return True
    # ooo, ooo, xxx
    elif board[2][0] == board[2][1] == board[2][2] == sign:
        return True
    # xoo, xoo, xoo
    elif board[0][0] == board[1][0] == board[2][0] == sign:
        return True
    # oxo, oxo, oxo
    elif board[0][1] == board[1][1] == board[2][1] == sign:
        return True
    # oox, oox, oox
    elif board[0][2] == board[1][2] == board[2][2] == sign:
        return True
    # xoo, oxo, oox
    elif board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    # oox, oxo, xoo
    elif board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    else:
        return False

def draw_move(board):
    free_positions = make_list_of_free_fields(board)
    random_index = randrange(len(free_positions))

    position = free_positions[random_index]
    coordinates = position_dict[position]

    board[coordinates[0]][coordinates[1]] = "X"
    return board

position_dict = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

board = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

while len(make_list_of_free_fields(board)):
    display_board(board)
    board = enter_move(board)
    display_board(board)

    if victory_for(board, "O"):
        print("You won!")
        break
    if len(make_list_of_free_fields(board)) == 0:
        print("It's a tie!")
        break

    draw_move(board)
    if victory_for(board, "X"):
        print("You lost!")
        break
    if len(make_list_of_free_fields(board)) == 0:
        print("It's a tie!")
        break