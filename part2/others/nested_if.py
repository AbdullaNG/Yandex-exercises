x = input()
if len(x) < 8:
    print('Короткий!')
else:
    y = input()
    if len(x) >= 8 and x == y:
        print('OK')
    elif x != y:
        print('Различаются.')