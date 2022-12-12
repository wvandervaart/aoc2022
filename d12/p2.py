import collections
import string
 
inputFile = open('input.txt', 'r')
 
rows = [list(row) for row in inputFile.read().split("\n")]
 
elevation = {v: i for i, v in enumerate(string.ascii_lowercase)}

 
def distance(start):
    visited = set([start])
    q = collections.deque([(start[0], start[1], 0)])
 
    while q:
        r, c, d = q.popleft()

 
        for nr, nc in (r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1):
            if 0 <= nr < len(rows) and 0 <= nc < len(rows[0]): 
                if rows[nr][nc] == "a" and elevation[rows[r][c]] - elevation["a"] <= 1:
                    return d+1
                    
                elif rows[nr][nc] != "a" and (nr, nc) not in visited and elevation[rows[r][c]] - elevation[rows[nr][nc]] <= 1:
                    visited.add((nr, nc))
                    q.append((nr, nc, d + 1))
 
# part 2, reverse direction:
for r in range(len(rows)):
    for c in range(len(rows[r])):
        if rows[r][c] == "E":
            rows[r][c] = "z"
            print(distance((r, c)))