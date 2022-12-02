file = open('input.txt', 'r')
lines = file.readlines()
line = lines[0]
for i in range(0,len(line)-4):
    checklist = set()
    for j in range(0,14):
        checklist.add(line[i+j])
    if len(checklist) == 14:
        print(i+14)
        exit()