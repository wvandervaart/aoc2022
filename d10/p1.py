s = []
with open(r"input.txt") as f:
    for line in f.readlines():
        match line.strip().split(" "):
            case ["noop"]: s.append(['noop'])
            case d, a: s.append([d,int(a)])

counter = 0
clock = 1
x=1
addc = 0
tot = 0
while counter < len(s):
    if clock % 40 == 0: check = 40
    if clock % 40 != 0: check = clock % 40
    if check -1 in [x-1,x,x+1]:
        print('#', end = '')
    else:
        print(' ', end = '')
    if (clock % 40 ) == 0:
        print()
    if (clock -20) % 40 == 0:
        tot += clock*x
    match s[counter][0]:
        case 'noop': counter += 1; clock += 1
        case 'addx':
            if addc == 1:
                x+=s[counter][1]
                clock +=1
                counter +=1
                addc = 0
            else:
                addc = 1
                clock += 1
print("Part1:", tot)