from utils import *
# Solving grid
pic1 = "53..7.... 6..195... .98....6. 8...6...3 4..8.3..1 7...2...6 .6....28. ...419..5 ....8..79"
grid1 = parse(pic1)
print(picture(grid1))
print(grid1['A1'])
print(grid1['A9'])
print(picture(constrain(grid1)))
print(string_picture(constrain(grid1)))
# Example when constrain is not good enough (need a search strategy)
grid2 = parse("4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......")
print(picture(grid2))
print(picture(constrain(grid2)))
# Using search to solve the harder grid
print(picture(search(constrain(grid2))))