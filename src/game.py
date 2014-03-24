import copy
import random
from grid import randomGrid
from tile import Tile


class Game(object):
    def __init__(self, grid=None):
        super(Game, self).__init__()
        self.grid = grid
        if self.grid is None:
            self.grid = randomGrid()
        self.nextTileDeck = []
        self.nextTile = self.getNextTile()

    def __copy__(self):
        gameCopy = Game(copy.copy(self.grid))
        gameCopy.nextTile = self.nextTile
        return gameCopy

    def isStuck(self):
        return self.grid.isStuck()

    def refillNextTileDeck(self):
        # see http://blog.braceyourselfgames.com/post/76156777645/threes-strategies
        # TODO: handle "bonus card"
        assert len(self.nextTileDeck) == 0
        for val in (1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3):
            self.nextTileDeck.append(Tile(val))
        random.shuffle(self.nextTileDeck)

    def getNextTile(self):
        if len(self.nextTileDeck) == 0:
            self.refillNextTileDeck()
        return self.nextTileDeck.pop()

    def userInput(self, direction):
        self.grid.pushGrid(direction, self.nextTile)
        self.nextTile = self.getNextTile()
