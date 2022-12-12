import collections
import string
 
inputFile = open('input.txt', 'r')
 
rows = [list(row) for row in inputFile.read().split("\n")]
 
elevation = {v: i for i, v in enumerate(string.ascii_lowercase)}
 
def distance(start):
    # create visisted set
    visited = set([start])
    #create queue for BFS algo
    q = collections.deque([(start[0], start[1], 0)])
 
    while q:
        # get leftmost element from queue and split it in row, column, distance
        r, c, d = q.popleft()
        
        #check all surrounding pos
        for nr, nc in (r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1):
            #check bounds
            if 0 <= nr < len(rows) and 0 <= nc < len(rows[0]): 
                # if pos = E and elevation diff <= 1 solved, return distance
                if rows[nr][nc] == "E" and elevation["z"] - elevation[rows[r][c]] <= 1:
                    return d + 1
                #if pos != E, and pos not is visited, and posnew = posold <= 1, add pos to visited and add pos to queue
                elif rows[nr][nc] != "E" and (nr, nc) not in visited and elevation[rows[nr][nc]] - elevation[rows[r][c]] <= 1:
                    visited.add((nr, nc))
                    q.append((nr, nc, d + 1))
 
# part 1: find S in grid and start search for shortest path for E
for r in range(len(rows)):
    for c in range(len(rows[r])):
        if rows[r][c] == "S":
            rows[r][c] = "a"
            print(distance((r, c)))