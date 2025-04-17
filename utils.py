# Ideas implemented from https://github.com/norvig/pytudes/blob/main/ipynb/Sudoku.ipynb (Peter Norvig Sudoku solver)
from typing import Dict
def pair(A: str, B: str) -> tuple:
    """
    Cross product of chars in string A and chars in string B.
    """
    return tuple(a + b for a in A for b in B)

Digit     = str  # e.g. '1'
digits    = '123456789'
DigitSet  = str  # e.g. '123'
rows      = 'ABCDEFGHI'
cols      = digits
Square    = str  # e.g. 'A9'
Grid      = Dict[Square, DigitSet] # E.g. {'A9': '123', ...}
Picture   = str
squares = pair(rows,cols) # Builds 81 square positions
all_boxes = [pair(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')] # Represents the 9 individual 3x3 grids
all_units = [pair(rows, c) for c in cols] + [pair(r, cols) for r in rows] + all_boxes # A list of all groupings
units     = {s: tuple(u for u in all_units if s in u) for s in squares} # For each square s, this maps box, row, col belonging to s
peers     = {s: set().union(*units[s]) - {s} for s in squares} # Get set of peers that are different from s

def is_solution(solution: Grid, puzzle: Grid) -> bool:
    """
    Checking the validity of a possible solution.
    :param solution: a possible sudoku solution
    :param puzzle: the sudoku we are trying to solve
    :return: a boolean depending on whether the solution is valid or not.
    """
    return (solution is not None and 
            all(solution[s] in puzzle[s] for s in squares) and 
            all({solution[s] for s in unit} == set(digits) for unit in all_units))

print(units['C2']) 
