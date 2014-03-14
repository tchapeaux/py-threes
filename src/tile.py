class Tile(object):
    """A tile of the grid"""
    def __init__(self, value):
        super(Tile, self).__init__()
        self.value = value

    def __repr__(self):
        return str(self.value)

    def merge(self, other):
        if other is None:
            return self
        if self.value > 2 and self.value == other.value:
            return Tile(2 * self.value)
        if (self.value == 1 and other.value == 2) or (self.value == 2 and other.value == 1):
            return Tile(3)
        return None
