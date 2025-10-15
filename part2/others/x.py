'''n = int(input())
y = 0
for x in range(1, n + 1):
	y = x * n + n
'''

n = int(input())
nmax = int((2 * n) ** (1 / 2))
for i in range(nmax, 0, -1) :
    if (2 * n - i * i + i) % (2 * i) == 0 :
        print((2 * n - i * i + i) // (2 * i))
        break