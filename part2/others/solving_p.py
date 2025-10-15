n = int(input())
p = 0
for x in range(0, n):
	y = 4 * ((-1) ** x) / (2 * x + 1)
	p += y
print(p)