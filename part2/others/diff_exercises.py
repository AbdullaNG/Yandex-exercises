start = int(input())
stop = int(input())
step = int(input())
for i in range(start, stop + 1, step):
	for j in range(start, stop + 1, step):
		print(f'{i} + {j} = {i + j}', end='\t')
	print()