n = int(input())
count = 0
while n != 1:
    count += 1
    if n % 2 != 0:
        n = 3 * n + 1
    else:
        n /= 2
print(count)