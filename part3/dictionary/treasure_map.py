n = int(input())
d = {}

for i in range(n):
	x = input().split()
	y = int(x[1])
	x = int(x[0])
	diff = (x // 10, y // 10)
	if diff in d:
		d[diff] += 1
	else:
		d[diff] = 1

print(max(d.values()))