from collections import Counter
file = open('input.txt', 'r')
lines = file.readlines()

tot = 0
for line in lines:
    d1 = Counter(line[:len(line)//2])
    d2 = Counter(line[len(line)//2:])
    comd = d1 & d2
    itemnr = ord(list(comd.elements())[0])
    if itemnr > 96:
        itemnr -= 96
    else:
        itemnr -= 38
    tot += itemnr
print(tot)