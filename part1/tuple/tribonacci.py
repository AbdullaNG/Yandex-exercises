n = int(input())
trib = [1, 1, 1]
summ = 0

for i in range (n - 3):
	for j in trib[-3:]:
		summ += j
	trib.append(summ)
	summ = 0

for x in trib:
	if n >= 3:
		print(x, end=' ')

if n <= 2:
	print('1 ' * n)