from math import sqrt

def walk(cmds) -> int:
    rope = [(0,0),(0,0)]
    dir_map = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
    tvis = set()
    tvis.add(rope[0])
    oh = [(0,0)]
    for command in cmds:
        # take steps
        for a in range(0,command[1]):
            oh[-1] = rope[-1]
            rope[-1] = (rope[-1][0] + dir_map[command[0]][0], rope[-1][1] + dir_map[command[0]][1])
            head = rope[-1]
            tail = rope[0]
            dist = sqrt((head[0] - tail[0]) ** 2 + (head[1] - tail[1]) ** 2)
            if dist < 2.0:continue
            tail = oh[-1]
            rope[0] = tail
            tvis.add(rope[0])
    return len(tvis)

s = []
with open(r"input.txt") as f:
    for line in f.readlines():
        match line.strip().split(" "):
            case d, a: s.append([d,int(a)])

print(walk(s))

