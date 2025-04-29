# Ideas implemented from https://github.com/norvig/pytudes/blob/main/ipynb/Sudoku.ipynb (Peter Norvig Sudoku solver)
from typing import Dict, Optional
import re
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

def constrain(grid) -> Grid:
    """
    Propogate constraints on a copy of grid to yield a new constrained Grid.
    :param grid: the grid we want to apply constraints to
    :return: a new constrained grid
    """
    result: Grid = {s: digits for s in squares}
    for s in grid:
        if len(grid[s]) == 1:
            fill(result, s , grid[s])
    return result

# If a unit has only one possible square that can hold a digit, then fill the square with the digit
def fill(grid: Grid, s: Square, d: Digit) -> Optional[Grid]:
    """
    Eliminate all the digits except d from grid[s].
    :param grid: the grid we want to update
    :param s: the given square we want modify
    :param d: the digit we want to fill at square s
    :return: None or the updated grid
    """
    if grid[s] == d or all(eliminate(grid, s , d2) for d2 in grid[s] if d2 != d):
        return grid
    else:
        return None
    
def eliminate(grid: Grid, s: Square, d: Digit) -> Optional[Grid]:
    """
    Eliminate d from grid[s]; implement the two constraint propagation strategies.
    :param grid: the grid we are updating
    :param s: the grid square are manipulating
    :param d: the digit we are concerned with
    """
    if d not in grid[s]:
        return grid # Already eliminated
    grid[s] = grid[s].replace(d, '')
    if not grid[s]:
        return None # None: no legal digit left
    elif len(grid[s]) == 1:
        #1. If a square has only one possible digit, then eliminate that digit as a possibility for each of the square's peers.
        d2 = grid[s]
        if not all(eliminate(grid, s2, d2) for s2 in peers[s]):
            return None # None: can't eliminate d2 from some square
    for u in units[s]:
        dplaces = [s for s in u if d in grid[s]]
        # 2. If a unit has only one possible square that can hold a digit, then fill the square with the digit.
        if not dplaces or (len(dplaces) == 1 and not fill(grid, dplaces[0], d)):
            return None # None: no place in u for d
    return grid

def parse(picture) -> Grid:
    """
    Convert a picture to a grid.
    :param picture: the string representation of a grid
    :return: the grid representation
    """
    vals = re.findall(r"[.1-9]|[{]1-9]+[}]", picture)
    return {s: digits if v == '.' else re.sub(r"[{}]", '', v) 
            for s, v in zip(squares, vals)}

def picture(grid) -> Picture:
    """
    Convert a grid into a picture string.
    :param grid: the grid we want to represent as a picture
    :return: a picture representation of a grid
    """
    if grid is None:
        return "None"
    def val(d: DigitSet) -> str: return '.' if d == digits else d if len(d) == 1 else '{' + d + '}'
    maxwidth = max(len(val(grid[s])) for s in grid)
    dash1 = '-' * (maxwidth * 3 + 2)
    dash2 = '\n' + '+'.join(3 * [dash1])
    def cell(r,c): return val(grid[r + c]).center(maxwidth) + ('|' if c in '36' else ' ') 
    def line(r): return ''.join(cell(r,c) for c in cols) + (dash2 if r in 'CF' else '')
    return '\n'.join(map(line, rows))

def search(grid) -> Grid:
    """
    Depth-first search with constraint propagation to find a solution.
    :param grid: the grid we want to solve
    :return: None, a completed grid, or a partially solved grid
    """
    if grid is None:
        return None
    s = min((s for s in squares if len(grid[s]) > 1),
        default=None, key=lambda s: len(grid[s]))
    if s is None: # No squares with multiple possibilities; the search has succeeded
        return grid
    for d in grid[s]:
        solution = search(fill(grid.copy(), s, d))
        if solution:
            return solution
    return None