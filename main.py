from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(0, len(board)):
        print(("+" + 7 * "-") * 3 + "+")
        print("|       " * 3 + "|")
        for j in range(0, len(board)):
            print("|" + " " * 3 + board[i][j], end=" " * 3)
        print("|")
        print("|       " * 3 + "|")
    print(("+" + 7 * "-") * 3 + "+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        move = input("Enter your input: ")
        try:
            if int(move) in range(1, 10):
                i, j = play_board_numbers[int(move)]
                if board[i][j] not in ("X", "O"):
                    board[i][j] = "O"
                    return board
                else:
                    print("Position already occupied")
                    continue
            else:
                print("Invalid position")
        except ValueError as error:
            print("Invalid input:", error)
            print("Please enter input in 1-9 ")

        return board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] not in ["X", "O"]:
                free_fields.append((i, j))
    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if (
        # logic for horizontal match
        (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign)
        or (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign)
        or (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign)
        # logic for vertical match
        or (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign)
        or (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign)
        or (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign)
        # logic for diagonal match
        or (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign)
        or (board[2][0] == sign and board[1][1] == sign and board[0][2] == sign)
    ):
        return True
    else:
        return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    if len(free_fields) == 0:
        print("Draw!")
        return board
    elif len(free_fields) == 9:
        board[1][1] = "X"
    else:
        computer_choice = randrange(len(free_fields))
        i, j = free_fields[computer_choice]
        board[i][j] = "X"
    return board


play_board_numbers = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}


play_board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
display_board(play_board)
while True:
    play_board = draw_move(play_board)
    print("Computer has entered. Your Turn")
    display_board(play_board)
    if victory_for(play_board, "X") is not True:
        if len(make_list_of_free_fields(play_board)) == 0:
            print("Draw")
            break
        play_board = enter_move(play_board)
        display_board(play_board)
        if victory_for(play_board, "O") is True:
            print("You won!!")
            break
    else:
        print("Computer won!!")
        break
