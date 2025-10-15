txt = input().split()
maxx = len(txt[0])
for i in range(len(txt)):
	if len(txt[i]) > maxx:
		maxx = len(txt[i])

txt = list(map(lambda x: '*' * (maxx - len(x)) + x, txt))
for j in txt:
	print(j)