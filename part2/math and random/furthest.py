import math


def d(x, y):
	return math.sqrt(x ** 2 + y ** 2)


n = int(input())
lt = []
for i in range(n):
	x = float(input())
	y = float(input())
	lt.append(d(x, y))

print(math.floor(max(lt) * 1000) / 1000)