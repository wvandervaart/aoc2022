#!/usr/bin/env python3

import sys


import numpy as np

with open("input.txt", "r") as f:
    grid = list(map(str.strip, f.readlines()))

R = len(grid)
C = len(grid[0])

visgrid = np.zeros((99, 99), dtype=int)



for r in range(R):
    
    for c in range(C):
        
        # check edge cases
        if c == 0 or c == C-1 or r == 0 or r == R-1:
            visgrid[r][c] = 1
        else:
            # check columns up to pos
            higher = 0
            for nc in range(0,c):
                if grid[r][c] <= grid[r][nc] and nc != c:
                    higher += 1
            if higher == 0:
                visgrid[r][c] = 1

            higher = 0
            for nc in range(c,C):
                if grid[r][c] <= grid[r][nc] and nc != c:
                    higher += 1
            if higher == 0:
                visgrid[r][c] = 1
            higher = 0
            for nr in range(0,r):
                if grid[r][c] <= grid[nr][c] and nr != r:
                    higher += 1
            if higher == 0:
                visgrid[r][c] = 1
            higher = 0
            for nr in range(r,R):
                if grid[r][c] <= grid[nr][c] and nr != r:
                    higher += 1
            if higher == 0:
                visgrid[r][c] = 1
              
            
print('p1',sum(sum(visgrid)))

