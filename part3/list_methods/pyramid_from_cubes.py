n = int(input())

for i in range(n):
	txt = [int(i) for i in input().split()]
	ind = txt.index(min(txt))
	flag = True

	for i in range(ind):
		flag = flag and (txt[i] >= txt[i + 1])
	for i in range(ind, len(txt) - 1):
		flag = flag and (txt[i] <= txt[i + 1])

	if flag:
		txt.sort(reverse=True)
		for z in txt:
			print(z, end=' ')
		print()
	else:
		print('НЕТ')