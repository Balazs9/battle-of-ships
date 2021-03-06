import random
from random import randint
import sys
from termcolor import colored, cprint


player_board = []
computer_board = []


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
for x in range(1, 6):
    player_board.append(["."] * 5)
    computer_board.append(["."] * 5)


def print_player_board():
    print(" ", " ".join("12345"))
    for letter, row in zip("ABCDE", player_board):
        print(letter, (" ").join(row))


def print_computer_board():
    print(" ", " ".join("12345"))
    for letter, row in zip("ABCDE", computer_board):
        print(letter, (" ").join(row))


print_player_board()
print("---------")
print_computer_board()


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


ship_comp_row_num = random_row(player_board)
ship_comp_col_num = random_col(player_board)
ship_player_row_num = random_row(computer_board)
ship_player_col_num = random_col(computer_board)


def take_turn(game):
    """
    Taking turns between player and computer
    """
    if game == 5:
        print("Game Over")
    else:
        game += 1


def guess_player_number(player_name):
    """
    Player guess the numbers
    """
    for game in range(5):
        print("Game", game + 1)
        print("Number must be between 1 and 5! \n")
        guess_row = input("guess row: \n")      # Let's the player guess the row number
        guess_col = input("guess column: \n")   # Let's the player guess the column number
        while guess_validate([guess_row, guess_col]) is False:
            guess_row = input("guess row: \n")
            guess_col = input("guess column: \n")

        guess_row = int(guess_row) - 1
        guess_col = int(guess_col) - 1

        if guess_row == ship_comp_row_num and guess_col == ship_comp_col_num:
            computer_board[guess_row][guess_col] = "o"
            print("Congratulations you found my ship! That was nice!")
            print_computer_board()
            break
        else:
            if (guess_row < 0 or guess_row > 4) or \
             (guess_col < 0 or guess_col > 4):
                print("Wrong! number must be equal or smaller than 5!")
            elif (computer_board[guess_row][guess_col] == "x"):
                print("you hit that already")
            else:
                print("Sorry, you missed my ship! Don't give up!")
                computer_board[guess_row][guess_col] = "x"
            print_computer_board()
            computer_result = guess_computer_number()
            if computer_result:
                print("Computer has Won!")
                break
            if game == 5:
                print("Game over")
            game += 1


def guess_computer_number():
    """
    Computer guess numbers to find the ship
    """
    guess_row = random.randint(0, 4)
    guess_col = random.randint(0, 4)

    if guess_row == ship_player_row_num and guess_col == ship_player_col_num:
        player_board[guess_row][guess_col] = "o"
        print_player_board()
        return True
    else:
        if (guess_row < 0 or guess_row > 4) or \
         (guess_col < 0 or guess_col > 4):
            print("Wrong! number must be equal or smaller than 5!")
        elif (player_board[guess_row][guess_col] == "z"):
            print("you hit that already")
        else:
            print("Sorry, you missed my ship! Don't give up!")
            player_board[guess_row][guess_col] = "z"
        print_player_board()
        return False


def guess_validate(values):
    """
    Player guess the row and the columns
    validator checks if it is an integer,
    if not ValueError
    """
    try:
        for value in values:
            value = int(value)

            if (value < 1 or value > 5):
                raise ValueError(
                    f"Values must be between 1 and 5, you provided {value}"
                )
    except ValueError as e:
        print(f"Sorry: {e}, it is not a number, try again please!")
        return False


def print_name(name):
    print(f"Hello {name}")


def main():
    """
    This is the function what runs the game
    """
    print("***********************************")
    print(colored("**Let's play the battle of ships!**", "yellow"))
    print("***********************************")
    print("***********************************")
    print(colored("Game rules: ", "yellow"))
    print(colored("Two players game, human against the computer.", "yellow"))
    print(colored("Each player guess their number.", "yellow"))
    print(colored("Then the bets will be visible on the boards.", "yellow"))
    print(colored("Each player has 5 chance to bet", "yellow"))
    print("***********************************")
    print(colored("Good luck and have fun!", "red"))
    print("***********************************")
    size = 5
    num_ships = 2
    game = 4
    print(f"Board size: {size}.\nNumber of ships: {num_ships}")
    player_name = input("Please enter your name: ")
    print_name(player_name)
    guess_player_number(player_name)
    guess_computer_number()
    take_turn(game)


main()
