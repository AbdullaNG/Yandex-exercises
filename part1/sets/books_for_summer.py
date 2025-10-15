M = int(input())
N = int(input())
mset = set()

for x in range(M):
	book = input()
	mset.add(book)

for y in range(N):
	book = input()
	if book in mset:
		print('YES')
	else:
		print('NO')