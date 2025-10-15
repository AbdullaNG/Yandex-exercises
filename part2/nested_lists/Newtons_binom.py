n = int(input())
lt = [1]

for i in range(n):
    for j in lt:
        print(j, end=' ')
    print()
    lt1 = [1]
    lt1 +=[lt[x] + lt[x + 1] for x in range(len(lt) - 1)] + [1]
    lt = lt1