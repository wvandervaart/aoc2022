file = open('input.txt', 'r')
lines = file.readlines()
line = lines[0]
for i in range(0,len(line)-4):
    checklist = set()
    for j in range(0,4):
        checklist.add(line[i+j])
    if len(checklist) == 4:
        print(i+4)
        exit()