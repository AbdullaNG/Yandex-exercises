N = int(input())
M = int(input())
nmset = set()
count = 0
newset = set()

for nm in range(N + M):
	both = input()
	if both not in nmset:
		count += 1
		newset.add(both)
	else:
		count -= 1
	nmset.add(both)

if count:
	print(count)
else:
	print('NO')