x = float(input())
summ = 0
while x >= 0:
    if x > 1000:
        x = x - x * 0.05
    summ += x
    x = float(input())
print(summ)
