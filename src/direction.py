class Direction(object):
    """Indicates a displacement direction"""
    def __init__(self, x, y):
        super(Direction, self).__init__()
        assert abs(x) == 1 or abs(y) == 1
        assert abs(x) + abs(y) == 1
        self.x = x
        self.y = y

    def __repr__(self):
        return "dir(" + str(self.x) + ", " + str(self.y) + ")"

    def __str__(self):
        dirString = ""
        if self.y == 1:
            dirString += "DOWN"
        elif self.y == -1:
            dirString += "UP"
        if self.x == 1:
            dirString += "RIGHT"
        elif self.x == -1:
            dirString += "LEFT"
        return dirString

global DIRECTIONS
DIRECTIONS = {
    'up': Direction(0, -1),
    'down': Direction(0, 1),
    'left': Direction(-1, 0),
    'right': Direction(1, 0)
}
