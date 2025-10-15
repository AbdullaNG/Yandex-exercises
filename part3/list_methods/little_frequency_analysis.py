txt = input().lower()
maxx = txt.count(txt[0])
x = txt[0]
alph = []
count = 0

for i in txt[1:]:
	if txt.count(i) > maxx and i != ' ':
		x = i
		maxx = txt.count(i)
	elif txt.count(i) == maxx:
		count = 1
	if count:
		alph.append(i)
	count = 0

if alph:
	j1 = alph[0]
	minn = j1
	
	for j in alph[1:]:
		if j < j1:
			minn = j
		j1 = j

if alph:
	print(minn)
else:
	print(x)