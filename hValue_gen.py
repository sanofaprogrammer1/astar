import math
import os.path
import grid_generator
def generate_hValue(grid, i, j): #i and j are the indices of goal state. Goal state is at position (i,j)
    for k in range(0, grid.length):
        for n in range(0, grid[k].length):
            grid[k][n].hValue = (abs(k-i) + abs(n-j))