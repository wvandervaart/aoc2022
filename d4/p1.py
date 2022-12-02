import re
file = open('input.txt', 'r')
lines = file.readlines()

count = 0 
for line in lines:
    e1s, e1e, e2s, e2e = [int(x) for x in re.split(',|-',line.strip())]
    if (e1s <= e2s and e1e >= e2e) or (e1s >= e2s and e1e <= e2e):
        count += 1
print(count)
