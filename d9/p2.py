from math import sqrt

def walk(cmds: list) -> int:
    rope = [(0,0)] * 10
    dir_map = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    tvis = set()
    tvis.add(rope[0])
    
    for command in cmds:
        rope[-1] = (rope[-1][0] + command[1] * dir_map[command[0]][0], rope[-1][1] + command[1] * dir_map[command[0]][1])

        moved = True
        while moved:
            moved = False
            for i in range(len(rope) - 1, 0, -1):
                rs = rope[i]
                er = rope[i-1]
                # check distance
                dft = sqrt((rs[0] - er[0]) ** 2 + (rs[1] - er[1]) ** 2)
                if dft < 2.0: break
                # er takes one step towards rs
                er = (er[0] + step(rs[0], er[0]), er[1] + step(rs[1], er[1]))
                moved = True
                rope[i-1] = er
            tvis.add(rope[0])
    return len(tvis)


def step(a, b) -> int:
    if a - b < 0: return -1
    if a - b > 0: return 1
    if a == b: return 0
    

cmds = []
with open(r"input.txt") as f:
    for line in f.readlines():
        cmds.append([line.split()[0],int(line.split()[1])])


print ("Part 2: {}".format(walk(cmds)))