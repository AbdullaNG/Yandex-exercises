x = input()
da = 0
net = 0
while x != '':
    if x == 'да':
        yes = x
        da += 1
    else:
        no = x
        net += 1
    x = input()
if (da + net) * 0.8 <= da:
    print('Достигли')
else:
    print('Пока нет')