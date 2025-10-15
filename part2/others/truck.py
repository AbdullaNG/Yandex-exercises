num = int(input())
count = 1
maxx = 0

for z in range(num):
	c = int(input())
	m = 100000000
	for x in range(c):
		height = int(input())
		if m > height:
			m = height
	if maxx < m:
		maxx = m
		count = z + 1
print(count, maxx)