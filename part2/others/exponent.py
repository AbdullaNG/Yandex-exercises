num = int(input())
if num % 2 == 0 and num % 4 == 0 or num == 2:
    y = 0
    while num != 1:
        num /= 2
        y += 1
    print(f'2\'s exponent {y}')
else:
    print('НЕТ')