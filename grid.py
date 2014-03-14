class Grid(object):
    """Represent a grid of tiles"""
    def __init__(self, sizeX, sizeY):
        super(Grid, self).__init__()
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.grid = [[None for j in range(sizeY)] for i in range(sizeX)]

    def __repr__(self):
        gString = ""
        for j in range(self.sizeY):
            for i in range(self.sizeX):
                gString += str(self.grid[i][j]) + "\t"
            gString = gString[:-1]
            gString += "\n"
        return gString[:-1]

    def isValid(self, i, j):
        return 0 <= i < self.sizeX and 0 <= j < self.sizeY, str(i) + ", " + str(j)

    def occupied(self, i, j):
        assert self.isValid(i, j)
        return self.grid[i][j] is not None

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
