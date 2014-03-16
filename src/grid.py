from direction import DIRECTIONS
from tile import Tile
import math
import random


class Grid(object):
    """Represent a grid of tiles"""
    @staticmethod
    def tileScore(value):
        # based on http://en.wikipedia.org/wiki/Threes!#Gameplay
        if value < 3:
            return 0
        elif value % 3 == 0:
            power = math.log(value // 3, 2) + 1
            return pow(3, power)
        else:
            raise AssertionError("Tile has invalid value: " + str(value))

    def __copy__(self):
        copyGrid = Grid(self.sizeX, self.sizeY)
        for i, j, cell in self.tileIterator():
            if self.occupied(i, j):
                copyGrid.putTile(i, j, cell)
        return copyGrid

    def __init__(self, sizeX, sizeY):
        super(Grid, self).__init__()
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.grid = [[None for j in range(sizeY)] for i in range(sizeX)]

    def __repr__(self):
        gString = ""
        for j in range(self.sizeY):
            for i in range(self.sizeX):
                gString += str(self.grid[i][j]) if self.grid[i][j] else "0"
                gString += "\t"
            gString = gString[:-1]
            gString += "\n"
        return gString[:-1]

    def tileIterator(self):
        for i, col in enumerate(self.grid):
            for j, cell in enumerate(col):
                yield i, j, cell

    def score(self):
        score = 0
        for i, j, cell in self.tileIterator():
            if cell is not None:
                score += Grid.tileScore(cell.value)
        return int(score)

    def isValid(self, i, j):
        return 0 <= i < self.sizeX and 0 <= j < self.sizeY

    def occupied(self, i, j):
        assert self.isValid(i, j)
        return self.grid[i][j] is not None

    def getTile(self, i, j):
        assert self.isValid(i, j)
        return self.grid[i][j]

    def putTile(self, i, j, newTile):
        if not self.occupied(i, j):
            self.grid[i][j] = newTile
        else:
            raise AssertionError("Tile is occupied")

    def moveTile(self, i, j, direction):
        """returns True if move is successful, False otherwise"""
        assert self.isValid(i, j)
        if self.occupied(i, j):
            newX, newY = i + direction.x, j + direction.y
            assert self.isValid(newX, newY)
            newTile = self.grid[i][j].merge(self.grid[newX][newY])
            if newTile is not None:
                self.grid[newX][newY] = newTile
                self.grid[i][j] = None
                return True
            else:
                return False
        else:
            return False

    def pushGrid(self, direction, newTile):
        # the order at which the tiles are treated depends on the direction
        colRange = list(range(self.sizeX))
        rowRange = list(range(self.sizeY))
        if direction.x == 1:
            colRange = list(reversed(colRange))
        if direction.y == 1:
            rowRange = list(reversed(rowRange))
        # we remove the row or column which does not move
        if direction.x != 0:
            colRange = colRange[1:]
        if direction.y != 0:
            rowRange = rowRange[1:]
        # use flags to detect rows/cols where at least one move was successful
        moveFlagsCol = [False for i in range(self.sizeX)]
        moveFlagsRow = [False for i in range(self.sizeY)]
        for i in colRange:
            for j in rowRange:
                success = self.moveTile(i, j, direction)
                if success:
                    moveFlagsCol[i] = True
                    moveFlagsRow[j] = True
        # adds the newTile in a row or col which moved (if any)
        movedCols = [i for i, moved in enumerate(moveFlagsCol) if moved]
        movedRows = [i for i, moved in enumerate(moveFlagsRow) if moved]
        if len(movedCols + movedRows) > 0:
            chosenRow = random.choice(movedRows)
            chosenCol = random.choice(movedCols)
            if direction == DIRECTIONS["left"]:
                self.putTile(self.sizeX - 1, chosenRow, newTile)
            elif direction == DIRECTIONS["right"]:
                self.putTile(0, chosenRow, newTile)
            elif direction == DIRECTIONS["up"]:
                self.putTile(chosenCol, self.sizeY - 1, newTile)
            elif direction == DIRECTIONS["down"]:
                self.putTile(chosenCol, 0, newTile)


def randomGrid():
    initialNumberOfTiles = 6
    g = Grid(4, 4)
    for n in range(initialNumberOfTiles):
        while True:
            x = random.randint(0, g.sizeX - 1)
            y = random.randint(0, g.sizeY - 1)
            if not g.occupied(x, y):
                break
        value = random.choice([1, 2, 3])
        g.grid[x][y] = Tile(value)
    return g
