r = int(input())
c = int(input())
obj = input()
for row in range(1, r + 1):
	for col in range(1, c + 1):
		if row == 1 or row == r:
			print(obj, end='')
		else:
			if col == 1 or col == c:
				print(obj, end='')
			else:
				print(' ', end='')
	print()