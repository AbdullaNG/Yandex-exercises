x = 0
y = 0
n = 0
flag = True
x1 = int(input())
y1 = int(input())
loc = input()
num = int(input())
while loc != 'стоп':
    if x1 == x and y1 == y:
        flag = False
    if loc == 'север':
        y += num
        if flag:
            n += 1
    elif loc == 'запад':
        x -= num
        if flag:
            n += 1
    elif loc == 'юг':
        y -= num
        if flag:
            n += 1
    elif loc == 'восток':
        x += num
        if flag:
            n += 1
    loc = input()
    if loc != 'стоп':
        num = int(input())
print(n)