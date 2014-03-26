from ai import ThreesAI
from direction import DIRECTIONS
from game import Game

import concurrent.futures


def aiTest():
    ai = ThreesAI(game=Game())
    ai.loop()
    return ai.game.grid.maxValue()

print("1) Launch AI")
print("2) Play yourself")
choice = input("Your choice? [1-2] ")

if choice == "1":
    maxValues = {}
    futures = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for i in range(100):
            futures.append(executor.submit(aiTest))
    for f in concurrent.futures.as_completed(futures):
        maxValue = f.result()
        if maxValue not in maxValues:
            maxValues[maxValue] = 0
        maxValues[maxValue] += 1
    print(maxValues)
elif choice == "2":
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
else:
    print("Did not get that. Exiting.")
