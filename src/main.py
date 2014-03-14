import random

from direction import DIRECTIONS
from grid import Grid
from tile import Tile


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

g = randomGrid()
print(g)
while True:
    nextPiece = Tile(random.choice([1, 2, 3]))
    validInput = False
    while not validInput:
        print("Next Piece:", nextPiece.value)
        userDirection = input("Direction? (up, down, left, right) ")
        try:
            if userDirection == "quit":
                exit(0)
            userDirection = DIRECTIONS[userDirection.lower()]
            validInput = True
        except KeyError as e:
            print("Invalid direction (" + str(userDirection) + ")")
    g.pushGrid(userDirection, nextPiece)
    print(g)
