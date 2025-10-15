txt = input()
count = 0
i1 = txt[0]
true = False

for i in txt:
	if i == i1:
		count += 1
	elif i != i1:
		print(count, i1)
		count = 1
		true = True
	i1 = i

print(count, i1)