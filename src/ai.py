import copy
import random
from direction import DIRECTIONS
from game import Game


class ThreesAI(object):
    """AI for the Threes game"""
    @staticmethod
    def score(grid):
        """ preference score of a Grid """
        # based on
        # http://forums.toucharcade.com/showpost.php?p=3136431&postcount=485
        score = 0
        for i, j, cell in grid.tileIterator():
            if cell is None:
                score += 4
            else:
                leftCell = grid[i - 1][j]
                rightCell = grid[i + 1][j]
                upCell = grid[i][j - 1]
                downCell = grid[i][j + 1]
                for neighbor in (leftCell, rightCell, upCell, downCell):
                    if neighbor and cell.value == neighbor.value:
                        score += 4
                if leftCell and rightCell and leftCell.value == rightCell.value:
                    score -= 1
                if upCell and downCell and upCell.value == downCell.value:
                    score -= 1
        return score

    def __init__(self, game=None, maxSteps=1000, testsPerSteps=100):
        # maxSteps: maximal number of moves
        # testsPerSteps: number of tests averaged for each direction
        super(ThreesAI, self).__init__()
        self.game = game if game else Game()
        self.maxSteps = maxSteps
        self.testsPerSteps = testsPerSteps
        self.currentStep = 0

    def loop(self):
        while self.currentStep <= self.maxSteps:
            self.step()
        print(self.game.grid)

    def step(self):
        print("(", self.currentStep, "-", self.game.grid.score(), ")")
        print(self.game.grid)
        # test each direction and find local best
        bestDir = []
        bestScore = 0
        for direction in DIRECTIONS.values():
            directionScore = 0
            for i in range(self.testsPerSteps):
                futureGame = copy.copy(self.game)
                futureGame.userInput(direction)
                directionScore += self.score(futureGame.grid)
            directionScore /= self.testsPerSteps
            if directionScore > bestScore:
                bestDir = []
            if len(bestDir) == 0 or directionScore == bestScore:
                bestDir.append(direction)
                bestScore = directionScore
        print("=>", bestDir)
        chosenDir = random.choice(bestDir)
        self.game.userInput(chosenDir)
        self.currentStep += 1
