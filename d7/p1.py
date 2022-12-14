from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)
for line in open('input.txt', 'r'):
    match line.split():
        case '$', 'cd', '/': c = ['']
        case '$', 'cd', '..': c.pop()
        case '$', 'cd', x: c.append(x)
        case '$', 'ls': pass
        case 'dir', _: pass
        case s, _:
            for d in accumulate(c):
                dirs[d] += int(s)

tot = 0
print(dirs)
for v in dirs.values():
    if v <= 100_000:
        print(v)
        tot += v
print(tot)