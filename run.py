from random import randint
from pprint import pprint

scores = {"computer": 0, "player": 0}

"""
Base of the game
"""

board = []
for x in range(5): 
    board.append([0]*5)

def __init__(self, size, num_ships, name, type):
    self.size = size
    self.board = [["." for x in range(size)] for y in range(size)]
    self.num_ships = num_ships
    self.name = name
    self.type = type
    self.guesses = []
    self.ships = []
    
def print_board(self, board):
    for row in self.board:
        print("".join(row))
    
print("Let's play the battle of ships")
print_board(board)
