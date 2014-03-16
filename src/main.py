import random

from direction import DIRECTIONS
from grid import randomGrid
from tile import Tile


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
    print("-----------------")
    print(g)
    print("-----------------")
