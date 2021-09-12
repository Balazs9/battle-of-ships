from random import randint
from pprint import pprint

scores = {"computer": 0, "player": 0}

"""
Base of the game
"""

board = []
for x in range(5): 
    board.append(["."]*5)

def print_board(board):
    for row in board:
        print((" ").join(row))


print("Let's play the battle of ships!")

print_board(board)

def guess_row_player():

    while True:
        print("number must be between 0 and 5!")
        data_row = input("enter your number:\n")

        if guess_validate(data_row):
            break

    return data_row

def guess_col_player():
    while True:
        print("number must be between 0 and 5!")
        data_col = input("enter your number:\n")

        if guess_validate(data_col):
            break

    return data_col


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

guess_row_player()
guess_col_player()
guess_validate()