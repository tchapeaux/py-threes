from direction import DIRECTIONS
from game import Game


g = Game()
while True:
    print("--------------")
    print(g.grid)
    print("--------------")
    print("Current Score:", g.grid.score())
    validInput = False
    while not validInput:
        print("Next Piece:", g.nextTile.value)
        userDirection = input("Direction? (up, down, left, right) ")
        try:
            if userDirection == "quit":
                exit(0)
            userDirection = DIRECTIONS[userDirection.lower()]
            validInput = True
        except KeyError as e:
            print("Invalid direction (" + str(userDirection) + ")")
    g.userInput(userDirection)
