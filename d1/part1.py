file = open('input.txt', 'r')
lines = file.readlines()

tot = 0
tots = []
for line in lines:
    if line != "\n":
        tot += int(line)
    else:
        tots.append(tot)
        tot = 0

tots.sort(reverse=True)
print(tots[0])
print(tots[0]+tots[1]+tots[2])