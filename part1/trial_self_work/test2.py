txt = input()
texts = []
texts.append(txt)
minn = len(txt)
maxx = len(txt)

for i in range(2):
	txt = input()
	if len(txt) > maxx:
		maxx = len(txt)
	elif len(txt) < minn:
		minn = len(txt)
	texts.append(txt)

for j in texts:
	if len(j) != minn and len(j) != maxx:
		midd = len(j)

for k in range(maxx, midd, -1 * minn):
	print(k, end=' ')
#------------------------EASY--------------------------