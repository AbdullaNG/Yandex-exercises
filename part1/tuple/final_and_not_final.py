n = int(input())
lt = []
s = 0
high = []
low = []

for i in range(n):
	name = input()
	score = int(input())
	lt.append((name, score))
	s += score

mid = s / n

for j in lt:
	if j[1] >= mid:
		high.append(j)
	else:
		low.append(j)


for x in range(len(high)):
	for x1 in range(len(high)):
		if high[x][0] < high[x1][0]:
			high[x], high[x1] = high[x1], high[x]

for y in high:
	print(y[0])

for a in range(len(low)):
	for a1 in range(len(low)):
		if low[a][0] < low[a1][0]:
			low[a], low[a1] = low[a1], low[a]

for b in low:
	print(b[0])