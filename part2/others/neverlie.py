x1 = 0
while (x := input()) != '':
    if len(x) >= 100:
        print(x1)
    elif len(x) < 100 and len(x) % 2 == 0:
        print(x * 2)
    elif len(x) < 100 and len(x) % 2 != 0 and len(x) % 3 == 0:
        print(x * 3)
    else:
        print(x)
    x1 = x