#!/usr/bin/env python3

import numpy as np

with open("input.txt", "r") as f:
    grid = list(map(str.strip, f.readlines()))

R = len(grid)
C = len(grid[0])

highers = []
for r in range(R):
    if r == 0 or r == R-1:
        continue
    
    for c in range(C):
        if c == 0 or c == C-1:
            continue
        # check columns up to pos
        h1,h2,h3,h4 = 0,0,0,0
        for nc in reversed(range(0,c)):
            if grid[r][c] <= grid[r][nc] and nc != c:
                h1+=1
                break
            else:
                h1+=1
        for nc in range(c,C-1):
            if grid[r][c] <= grid[r][nc] and nc != c:
                h2+=1
                break
            else:
                h2+=1
        for nr in reversed(range(0,r)):
            if grid[r][c] <= grid[nr][c] and nr != r:
                h3+=1
                break
            else:
                h3+=1
        for nr in range(r,R-1):
            if grid[r][c] <= grid[nr][c] and nr != r:
                h4+=1
                break
            else:
                h4+=1

        highers.append(h1*h2*h3*h4)

#print(highers)
print('p2',max(highers))

