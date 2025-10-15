n = int(input())
s = 0

for i in range(1, n + 1):
    summ = 0
    for x in range(1, i + 1):
        if x % 2 == i % 2:
            summ += x
    result = 1
    for y in range(summ):
        result *= i
    s += result
print(s)
