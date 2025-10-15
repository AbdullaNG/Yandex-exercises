n = int(input())
list1 = []

for i in range(n):
    txt = input()
    list1.append(txt)
num = int(input())

for j in list1:
    if num > len(j):
        continue
    else:
        print(j[num - 1], end='')