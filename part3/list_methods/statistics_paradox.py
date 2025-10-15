num = int(input())
medians = []
modes = []
all_nums = []

for j in range(num):
	n = [int(i) for i in input().split()]

	for take in n:
		all_nums.append(take)

	for a in range(len(n)):
		for b in range(len(n)):
			if n[a] < n[b]:
				n[a], n[b] = n[b], n[a]

	x = len(n)
	if x % 2 == 0:
		median = (n[int(x / 2) - 1] + n[int(x / 2 + 1) - 1]) / 2
	else:
		median = n[int((x + 1) / 2) - 1]
	medians.append(median)

	counts = [n.count(z) for z in n]
	mode = [y for y in n if n.count(y) == max(counts)]
	modes.append(mode[0])

for g in medians:
	print(g, end=' ')
print()

for k in modes:
	print(k, end=' ')
print()

medians.sort()
x = len(medians)
if x % 2 == 0:
	median = (medians[int(x / 2) - 1] + medians[int(x / 2 + 1) - 1]) / 2
else:
	median = medians[int((x + 1) / 2) - 1]
print(median)

counts = [modes.count(z) for z in modes]
mode = [y for y in modes if modes.count(y) == max(counts)]
print(mode[0])

all_nums.sort()
x = len(all_nums)
if x % 2 == 0:
	median = (all_nums[int(x / 2) - 1] + all_nums[int(x / 2 + 1) - 1]) / 2
else:
	median = all_nums[int((x + 1) / 2) - 1]
print(median)

counts = [all_nums.count(z) for z in all_nums]
mode = [y for y in all_nums if all_nums.count(y) == max(counts)]
print(mode[0])