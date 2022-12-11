import math

with open("input.txt", "r") as f:
    monkeys = f.read().split("\n\n")

def doCalc(calc,item, lcmNum):
    a,op,b = calc.split()
    if str(a) == 'old':
        a = item
    if str(b) == 'old':
        b = item    
    match op:
        case '+': return (int(a) + int(b))%lcmNum
        case '*': return (int(a) * int(b))%lcmNum


m = {}
for monkey in monkeys:
    for rule in monkey.split("\n"):
        start, var = rule.strip().split(":")
        match start.split():
            case 'Monkey', a: m[int(a)] = {}
            case 'Starting', _: m[int(a)]['items'] = [x.strip() for x in var.strip().split(',')]
            case ['Operation']: m[int(a)]['oper'] = var.split('=')[1]
            case ['Test']: m[int(a)]['test'] = int(var.split()[2])
            case 'If', 'true': m[int(a)]['t'] = int(var.split()[3])
            case 'If', 'false': m[int(a)]['f'] = int(var.split()[3])
        m[int(a)]['ac'] = 0

lcmNum = 1
for i in m:
    lcmNum = math.lcm(lcmNum, int(m[i]['test']))


iter = 0
while iter < 10000:
    for i in range(0,len(m)):
        for j in range(0, len(m[i]['items'])):
            it = m[i]['items'].pop()
            it = doCalc(m[i]['oper'], it, lcmNum)
            m[i]['ac'] += 1
            if it % m[i]['test'] == 0:
                m[m[i]['t']]['items'].append(it)
            else:
                m[m[i]['f']]['items'].append(it)
    iter +=1

activity = []
for i in range(0,len(m)):
    activity.append(m[i]['ac'])
activity = sorted(activity)
print((activity[-1] * activity[-2]))