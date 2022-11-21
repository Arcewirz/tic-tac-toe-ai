# tic_tac_toe/logic/models.py

import enum
import re
from dataclasses import dataclass
from functools import cached_property

class Mark(str, enum.Enum):
    CROSS = 'X'
    NAUGHT = 'O'

    @property
    def other(self) -> 'Mark':
        return Mark.CROSS if self is Mark.NAUGHT else Mark.NAUGHT


# Using frozen immutable objects due to fault tolerance and improved readability (new grid after each move).
# Ignoring not significant computation costs.
@dataclass(frozen=True)
class Grid:
    cells: str = ' ' * 9

    def __post_init__(self) -> None:
        if not re.match(r'^[\sXO]{9}$', self.cells):
            raise ValueError('Grid must contain 9 cells of: X or 0 or space')

    @cached_property
    def x_count(self) -> int:
        return self.cells.count('X')

    @cached_property
    def o_count(self) -> int:
        return self.cells.count('O')

    @cached_property
    def empty_count(self) -> int:
        return self.cells.count(' ')