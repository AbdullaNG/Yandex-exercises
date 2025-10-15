n = int(input())
tp = []
flag = False
count1 = 0
count2 = 0

for i in range(n):
    num = int(input())
    tp.append(num)
m = int(input())

for x in tp:
    count1 += 1
    for y in tp:
        count2 += 1
        if x * y == m and count1 != count2:
            flag = True
    count2 = 0

if flag:
    print('ДА')
else:
    print('НЕТ')