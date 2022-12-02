def getResult(a, b):
    winners = {'A':'Y', 'B':'Z','C':'X'}
    ties = {'A':'X', 'B':'Y','C':'Z'}
    points = {'X':1,'Y':2,'Z':3}
    #0,3,6
    if b == winners[a]:
        #winner
        return 6+points[b]
    elif b == ties[a]:
        #tie
        return 3+points[b]
    else:
        #loser
        return points[b]



file = open('input.txt', 'r')
lines = file.readlines()

count=0
for line in lines:
    p1, p2 = line.rstrip('\r\n').split(' ')
    count += getResult(p1, p2)
    print(getResult(p1, p2))
print("Total score: ", count)