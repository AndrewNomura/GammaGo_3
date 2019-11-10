import enum
from collections import namedtuple


__all__ = [
    'Player',
    'Point',
]


class Player(enum.Enum):
    black = 1
    white = 2

# black_score + white_score

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white
# end::color[]


# tag::points[]
class Point(namedtuple('Point', 'row col')):
    def neighbors(self):
        return [
            Point(self.row - 1, self.col),
            Point(self.row + 1, self.col),
            Point(self.row, self.col - 1),
            Point(self.row, self.col + 1),
        ]
# end::points[]

    def __deepcopy__(self, memodict=None):
        # These are very immutable.
        return self


