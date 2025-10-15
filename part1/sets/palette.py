many = set()
first = set()
c = 0
n = int(input())

for x in range(n):
	m = int(input())
	for y in range(m):
		z = input()
		if z in first:
			many.add(z)
			c += 1
		else:
			first.add(z)
l = len(many)
print(l, c + l)