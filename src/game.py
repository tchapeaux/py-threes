import random
from grid import randomGrid
from tile import Tile


class Game(object):
    def __init__(self, grid=None):
        super(Game, self).__init__()
        self.grid = grid
        if self.grid is None:
            self.grid = randomGrid()
        self.nextTile = self.getNextTile()

    def getNextTile(self):
        return Tile(random.choice([1, 2, 3]))

    def userInput(self, direction):
        self.grid.pushGrid(direction, self.nextTile)
        self.nextTile = self.getNextTile()
