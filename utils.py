# Ideas implemented from https://github.com/norvig/pytudes/blob/main/ipynb/Sudoku.ipynb (Peter Norvig Sudoku solver)

def pair(A, B):
    """
    Cross product of strings in A and strings in B.
    param A: A list of strings
    param B: A list of strings
    return: A tuple of the pairings 
    """
    return tuple(a + b for a in A for b in B)
