n = int(input())
lt = []
add = ['встал', 'встала', 'в', 'очередь.']
rep = ['Привет,', 'будет', 'за', 'тобой.'] 
rem = ['хватит', 'тут', 'стоять,', 'пошли', 'отсюда.']

for i in range(n):
    txt = input()
    if 'встал' in txt or 'встала' in txt:
        tp = ''
        for j in txt.split():
            if j not in add:
                tp = tp + j + ' '
        lt.append(tp.strip())
    elif 'Привет,' in txt:
        x = txt.split('! ')[0][8:]
        ind = lt.index(x)
        tp = ''
        for z in txt.split():
            if z not in rep and '!' not in z:
                if z == x:
                    tp += z + ' '
                if z not in x:
                    tp += z + ' '
        lt.insert(ind + 1, tp.strip())
    elif 'хватит' in txt:
        y = txt.split(', ')[0]
        lt.pop(lt.index(y))

for i in lt:
    print(i)