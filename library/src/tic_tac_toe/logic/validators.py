#tic_tac_toe/logic/validators.py

import re

from tic_tac_toe.logic.models import Grid

def validate_grid(grid: Grid) -> None:
    if not re.match(r'^[\sXO]{9}$', grid.cells):
        raise ValueError('Grid must contatin 9 cells of X or O or space')