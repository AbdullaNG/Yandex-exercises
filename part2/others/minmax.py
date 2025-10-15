'''
x = int(input())
x1 = x // 100
x2 = (x % 100) // 10
x3 = x % 10
if x1 > x2 and x1 > x3 and x2 > x3:
    maxx = x1
    midd = x2
    minn = x3
elif x1 > x2 and x1 > x3 and x3 > x2:
    maxx = x1
    midd = x3
    minn = x2
elif x1 > x2 and x1 > x3 and x2 == x3:
    maxx = x1
    midd = x3
    minn = x2
elif x1 > x2 and x1 == x3:
    maxx = x1
    midd = x3
    minn = x2
elif x1 > x3 and x1 == x2:
    maxx = x1
    midd = x2
    minn = x3
elif x2 > x1 and x2 > x3 and x1 > x3:
    maxx = x2
    midd = x1
    minn = x3
elif x2 > x1 and x2 > x3 and x3 > x1:
    maxx = x2
    midd = x3
    minn = x1
elif x2 > x1 and x2 > x3 and x1 == x3:
    maxx = x2
    midd = x3
    minn = x1
elif x2 > x1 and x1 == x3:
    maxx = x2
    midd = x1
    minn = x3
elif x3 > x1 and x3 > x2 and x1 > x2:
    maxx = x3
    midd = x1
    minn = x2
elif x3 > x1 and x3 > x2 and x2 > x1:
    maxx = x3
    midd = x2
    minn = x1
elif x3 > x2 and x3 > x1 and x2 == x1:
    maxx = x3
    midd = x1
    minn = x2
elif x3 > x1 and x1 == x2:
    maxx = x3
    midd = x2
    minn = x1
elif x3 > x1 and x3 == x2:
    maxx = x3
    midd = x2
    minn = x1
else:
    maxx = x3 or x1 or x2
    midd = x2 or x1 or x3
    minn = x1 or x2 or x3
if (maxx + minn) / 2 != midd:
    print('Жаль, вы ввели обычное число')
else:
    print('Вы ввели красивое число')
'''


x = int(input())
x1 = x // 100
x2 = (x % 100) // 10
x3 = x % 10
if x1 > x2 and x1 > x3 and x2 > x3:
    maxx = x1
    midd = x2
    minn = x3
elif x1 > x2 and x1 > x3 and x3 > x2:
    maxx = x1
    midd = x3
    minn = x2
elif x1 > x2 and x1 > x3 and x2 == x3:
    maxx = x1
    midd = x3
    minn = x2
elif x1 > x2 and x1 == x3:
    maxx = x1
    midd = x3
    minn = x2
elif x1 > x3 and x1 == x2:
    maxx = x1
    midd = x2
    minn = x3
elif x2 > x1 and x2 > x3 and x1 > x3:
    maxx = x2
    midd = x1
    minn = x3
elif x2 > x1 and x2 > x3 and x3 > x1:
    maxx = x2
    midd = x3
    minn = x1
elif x2 > x1 and x2 > x3 and x1 == x3:
    maxx = x2
    midd = x3
    minn = x1
elif x2 > x1 and x1 == x3:
    maxx = x2
    midd = x1
    minn = x3
elif x3 > x1 and x3 > x2 and x1 > x2:
    maxx = x3
    midd = x1
    minn = x2
elif x3 > x1 and x3 > x2 and x2 > x1:
    maxx = x3
    midd = x2
    minn = x1
elif x3 > x2 and x3 > x1 and x2 == x1:
    maxx = x3
    midd = x1
    minn = x2
elif x3 > x1 and x1 == x2:
    maxx = x3
    midd = x2
    minn = x1
elif x3 > x1 and x3 == x2:
    maxx = x3
    midd = x2
    minn = x1
else:
    maxx = x3 or x1 or x2
    midd = x2 or x1 or x3
    minn = x1 or x2 or x3
if minn == 0 and midd != 0:
    print(midd * 100 + maxx)
elif minn == 0 and midd == 0:
    print(maxx * 100)
else:
    print(minn * 100 + midd * 10 + maxx)