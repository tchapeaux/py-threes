from ai import ThreesAI
from direction import DIRECTIONS
from game import Game


print("1) Launch AI")
print("2) Play yourself")
choice = input("Your choice? [1-2] ")

g = Game()
if choice == "1":
    ai = ThreesAI(game=g)
    ai.loop()
elif choice == "2":
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
else:
    print("Did not get that. Exiting.")
