import re
with open("input.txt", "r") as f:
    stacks,moves = f.read().split("\n\n")

#create stacks
for i in range(1,10):
    globals()[f'st{i}'] = []

#fill stacks with original input
for c,line in enumerate(stacks.split('\n')):
    if '[' in line:
        for i in range(0,9):
        #1,5,9,13
            if line[i*4+1] != " ":
                globals()[f'st{i+1}'].insert(0, line[i*4+1])

#execute moves
for line in moves.split("\n"):
    a,mv,b,fr,c,to = line.split(" ")
    globals()[f'st{to}'] += list(globals()[f'st{fr}'][-int(mv):])
    globals()[f'st{fr}'] = globals()[f'st{fr}'][:-int(mv)]
    
#generate answer
answer = ''
for i in range(1,10):
    answer += globals()[f'st{i}'].pop()
print(answer)