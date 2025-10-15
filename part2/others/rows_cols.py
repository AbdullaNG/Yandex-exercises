c = int(input())
r = int(input())

for rows in range(1, r + 1):
	for cols in range(1, c + 1):
		print(float(cols / rows), end=' ')
	print()