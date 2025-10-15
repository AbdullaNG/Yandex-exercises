row = int(input())
col = int(input())
table = []
tp = []
count = 0

for i in range(row):
	for j in range(col):
		txt = input()
		tp.append(txt)
	table.append(tp)
	tp = []

for x in table:
	count += 1
	if count == 1 or count == len(table):
		for y in x:
			print(y, end='\t')
		print()
	else:
		x.sort()
		for y in x:
			print(y, end='\t')
		print()