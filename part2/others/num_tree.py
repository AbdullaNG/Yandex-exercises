N = int(input())
k = 1
c = 1
while k <= N:
	for i in range(0, c):
		if k > N:
			break
		print(k, end=(' '))
		k += 1
	c += 1
	print()