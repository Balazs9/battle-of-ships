from random import randint
from pprint import pprint

scores = {"computer": 0, "player": 0}

class Board:
    """
    Base of the game
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []
        

