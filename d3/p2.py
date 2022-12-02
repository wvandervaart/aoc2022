from collections import Counter

file = open('input.txt', 'r')
lines = file.readlines()
lines = [lines[i:i + 3] for i in range(0, len(lines), 3)]

tot = 0
for line in lines:
    d1,d2,d3 = Counter(line[0]), Counter(line[1]), Counter(line[2])
    comd = d1 & d2 & d3
    itemnr = ord(list(comd.elements())[0])
    if itemnr > 96:
        itemnr -= 96
    else:
        itemnr -= 38
    tot += itemnr
print(tot)