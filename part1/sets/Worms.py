newset = set()
n = int(input())

for x in range(n):
	worm = input()
	if worm in newset:
		print('ДА')
	else:
		print('НЕТ')
	newset.add(worm)
