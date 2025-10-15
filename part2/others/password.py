pswrd1 = ''
pswrd2 = ''
while (len(pswrd1) < 8 or pswrd1 != pswrd2 or
    (len(pswrd1) >= 8 and '123' in pswrd1)):
    pswrd1 = input()
    pswrd2 = input()
    if len(pswrd1) >= 8 and '123' in pswrd1:
        print('Простой!')
    elif len(pswrd1) < 8:
        print('Короткий!')
    elif pswrd1 != pswrd2:
        print('Различаются.')
print('OK')