n = int(input())
summ = 0

for m in range(1, n + 1):
	summ += len(str(m))
	if summ >= n:
		print(m)
		break