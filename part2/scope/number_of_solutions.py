def fac(n):
    if n == 0 or n == 1:
        return 1
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def solve():
    x = 3
    x1 = fac(n + x - 1)
    x2 = fac(n) * fac(x - 1)
    return x1 // x2


n = 100
print(solve())