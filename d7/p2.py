from collections import defaultdict
from itertools import accumulate

dirs = defaultdict(int)
for line in open('input.txt', 'r'):
    match line.split():
        case '$', 'cd', '/': c = [''] #create root
        case '$', 'cd', '..': c.pop() #move up 1 dir
        case '$', 'cd', x: c.append(x) #go down 1 dir
        case '$', 'ls': pass #not usefull
        case 'dir', _: pass #also not usefull
        case s, _: #take size from files
            for d in accumulate(c): # merge dirnames to one string
                dirs[d] += int(s) # add filesize to dir

tot = []
for v in dirs.values(): #loop over dir sizes
    if v >= dirs['']-40_000_000: # check if dir frees up enough space 70_000_000-30_000_000
        tot.append(v) # append dir to list
print(min(tot))

print(dirs)