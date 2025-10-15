txt = input()
if txt == 'ясно':
    tp = [1.0, 0.0]
else:
    tp = [0.0, 1.0]

n1 = float(input())
n2 = float(input())
pred = [n1, n2]
n = int(input())

for i in range(n):
    mx1 = max(tp[0] * pred[0], tp[1] * (1.0 - pred[1]))
    mx2 = max(tp[1] * pred[1], tp[0] * (1.0 - pred[0]))
    tp = [mx1, mx2]

if tp[0] > tp[1]:
    print('ясно')
    print(tp[0])
elif tp[1] > tp[0]: 
    print('пасмурно')
    print(tp[1])
else:
    print('равновероятно')
    print(tp[0])