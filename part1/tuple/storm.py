lt = []
n = int(input())

for x in range(n):
    a = int(input())
    b = float(input())
    c = (a, b)
    lt.append(c)
 
for i in range(len(lt) - 1):
    for j in range(len(lt) - 1 - i):
        if lt[j] > lt[j + 1]:
            lt[j], lt[j + 1] = lt[j + 1], lt[j]
    print(lt[j + 1])

minn = lt[0]
for z in lt:
    if z < minn:
        minn = z
print(minn)