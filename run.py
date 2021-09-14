import random
from random import randint
import sys
from termcolor import colored, cprint

board = []


player = {
    "name": "player_name",
    "wins": 0,
    "lose": 0
}
computer = {
    "name": "Computer",
    "wins": 0,
    "lose": 0
}
for x in range(0, 5):
    board.append(["."] * 5)


def print_player_board(board):
    for row in board:
        print((" ").join(row))


def print_computer_board(board):
    for row in board:
        print((" ").join(row))


print_player_board(board)
print("---------")
print_computer_board(board)


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_row_num = random_row(board)
ship_col_num = random_col(board)


def take_turn(game):
    """
    Taking turns between player and computer
    """
    if game == 4:
        print("Game Over")
    else:
        game += 1


def guess_player_number(player_name):
    """
    Player guess the numbers
    """
    for game in range(5):
        print("Game", game + 1)
        print("Number must be between 0 and 4! \n")
        guess_row = int(input("guess row: "))
        guess_col = int(input("guess column: "))

        # print(ship_row_num)
        # print(ship_col_num)

        if guess_row == ship_row_num and guess_col == ship_col_num:
            print("Congratulations you found my ship!")
            break
        else:
            if (guess_row < 0 or guess_row > 4) or \
             (guess_col < 0 or guess_col > 4):
                print("Wrong! number must be equal or smaller than 4!")
            elif (board[guess_row][guess_col] == "x"):
                print("you hit that already")
            else:
                print("you missed my ship!")
                board[guess_row][guess_col] = "x"
            print_player_board(board)
            return guess_computer_number


def guess_computer_number():
    """
    Computer guess numbers to find the ship
    """
    for game in range(5):
        print("Game", game + 1)
        print("number must be between 0 and 4!")
        guess_row = random.randint(0, 4)
        guess_col = random.randint(0, 4)

        if guess_row == ship_row_num and guess_col == ship_col_num:
            print("Congratulations you found my ship!")
            break
        else:
            if(guess_row < 0 or guess_row > 4) or \
             (guess_col < 0 or guess_col > 4):
                print("Wrong! number must be equal or smaller than 4!")
            elif (board[guess_row][guess_col] == "z"):
                print("you hit that already")
            else:
                print("you missed my ship!")
                board[guess_row][guess_col] = "z"
            print_computer_board(board)
            return guess_player_number


def guess_validate(values):
    """
    Player guess the row and the columns
    validator checks if it is an integer,
    if not ValueError
    """

    try:
        [int("value") for guess_row, guess_col in values]
        if "value" != 5:
            raise ValueError(f"Value must be smaller than 4, n\
                 you provided {value}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def main():
    print("***********************************")
    print("**Let's play the battle of ships!**")
    print("***********************************")
    size = 5
    num_ships = 2
    game = 4
    print(f"Board size: {size}.\nNumber of ships: {num_ships}")
    player_name = input("Please enter your name: ")
    guess_player_number(player_name)
    guess_computer_number()
    take_turn(game)


main()
