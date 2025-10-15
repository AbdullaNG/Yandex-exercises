n = [int(i) for i in input().split()]

for a in range(len(n)):
	for b in range(len(n)):
		if n[a] < n[b]:
			n[a], n[b] = n[b], n[a]

x = len(n)

median = n[int((x + 1) / 2) - 1]

counts = [n.count(z) for z in n]
mode = [y for y in n if n.count(y) == max(counts)]

print(median, mode[0])