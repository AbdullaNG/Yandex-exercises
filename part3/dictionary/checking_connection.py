txt = input().split()
d = {}

for i in txt:
	if i not in d.keys():
		d[i] = 1
		print(d[i], end=' ')
	else:
		d[i] += 1
		print(d[i], end=' ')