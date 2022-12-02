import re
file = open('input.txt', 'r')
lines = file.readlines()

count = 0 
for line in lines:
    e1s, e1e, e2s, e2e = [int(x) for x in re.split(',|-',line.strip())]
    start = max(e1s, e2s)
    end = min(e1e, e2e)
    if(end >= start):
        count += 1
print(count)
