n = [float(i) for i in input().split()]

for a in range(len(n)):
	for b in range(len(n)):
		if n[a] < n[b]:
			n[a], n[b] = n[b], n[a]

x = len(n)

if x % 2 == 0:
	median = (n[int(x / 2) - 1] + n[int(x / 2 + 1) - 1]) / 2
else:
	median = n[int((x + 1) / 2) - 1]

print(sum(n) / x, median)