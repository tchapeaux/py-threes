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
                leftCell = grid.getTile(i - 1, j) if grid.isValid(i - 1, j) else None
                rightCell = grid.getTile(i + 1, j) if grid.isValid(i + 1, j) else None
                upCell = grid.getTile(i, j - 1) if grid.isValid(i, j - 1) else None
                downCell = grid.getTile(i, j + 1) if grid.isValid(i, j + 1) else None
                for neighbor in (leftCell, rightCell, upCell, downCell):
                    if neighbor and cell.merge(neighbor) is not None:
                        score += 4
                if leftCell and rightCell and leftCell.value == rightCell.value:
                    score -= 1
                if upCell and downCell and upCell.value == downCell.value:
                    score -= 1
        return score

    def __init__(self, game=None, maxSteps=1000, testsPerSteps=100, verbose=False):
        # maxSteps: maximal number of moves
        # testsPerSteps: number of tests averaged for each direction
        super(ThreesAI, self).__init__()
        self.game = game if game else Game()
        self.maxSteps = maxSteps
        self.testsPerSteps = testsPerSteps
        self.verbose = verbose
        self.currentStep = 0

    def loop(self):
        while self.currentStep <= self.maxSteps and not self.game.isStuck():
            self.step()

    def step(self):
        if self.verbose:
            print("(", self.currentStep, "-", self.game.grid.score(), ")")
        # test each direction and find local best
        bestDir = []
        bestScore = 0
        for direction in [d for d in DIRECTIONS.values() if self.game.grid.canPush(d)]:
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
        assert len(bestDir) > 0
        chosenDir = random.choice(bestDir)
        if self.verbose:
            print(self.game.grid)
            print("=>", chosenDir)
        self.game.userInput(chosenDir)
        self.currentStep += 1
