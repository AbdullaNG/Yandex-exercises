n = int(input())
matrix = []
summ = 0

for i in range(n):
	txt = input().split(', ')
	summ += int(txt[i]) + int(txt[i * -1 - 1])
	txt[i], txt[i * -1 - 1] = txt[i * -1 - 1], txt[i]
	matrix.append(txt)

for x in matrix:
	for y in x:
		print(y, end=' ')
	print()

print(summ)