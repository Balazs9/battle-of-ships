from random import randint
from pprint import pprint

scores = {"computer": 0, "player": 0}

"""
Base of the game
"""

board = []
for x in range(0, 5): 
    board.append(["."] * 5)

def print_board(board):
    for row in board:
        print((" ").join(row))

print("Let's play the battle of ships!")

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row_num = random_row(board)

ship_col_num = random_col(board)


def guess_player_number():

    for game in range(5):
        print("Game"), game
        print("number must be between 0 and 4!")
        guess_row = int(input("guess row: "))
        guess_col = int(input("guess column: "))

        print(ship_row_num)
        print(ship_col_num)

        if guess_row == ship_row_num and guess_col == ship_col_num:
            print("Congratulations you found my ship!")
            break
        else:
            if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
                print("Wrong! number must be equal or smaller than 5!")
            elif (board[guess_row][guess_col] == "x"):
                print("you hit that already")
            else:
                print("you missed my ship!")
                board[guess_row][guess_col] = "x"  

guess_player_number()

def guess_computer_number():
    for game in range(5):
        print("Game"), game
        print("number must be between 0 and 4!")
        guess_row = int(input("guess row: "))
        guess_col = int(input("guess column: "))

        if guess_row == ship_row_num and guess_col == ship_col_num:
            print("Congratulations you found my ship!")
            break
        else:
            if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
                print("Wrong! number must be equal or smaller than 5!")
            elif (board[guess_row][guess_col] == "z"):
                print("you hit that already")
            else:
                print("you missed my ship!")
                board[guess_row][guess_col] = "z"  
        
guess_computer_number()

def guess_validate(values):
    """
    Player guess the row and the columns
    """

    try:
        [int(value) for value in values]
        if value >> 5:
            raise ValueError(
                f"Value must be smaller than 5"
            )
    except ValueError as e:
        print(f"Invalid data {e}, please try again.\n")
        return False

    return True



def new_game():
    """
    New game starts. Sets board size and number of ships.
    Reset the scoreboard
    """

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    print(f"Board size: {size}. Number of ships: {num_ships}")
    print("Top left corner is row: 0, col: 0")
    player_name = input("Please enter your name: \n")

new_game()
    