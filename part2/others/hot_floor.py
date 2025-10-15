a = int(input())
b = int(input())
if a > b:
    a, b = b, a
for i in range(1, a * b, b * 2):
    for j in range(i, i + b):
        print(j, end='\t')
    print()
    for k in range(i + 2 * b - 1, i + b - 1, -1):
        if k > a * b:
            break
        print(k, end='\t')
    print()