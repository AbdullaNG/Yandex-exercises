txt = 0
tp = []
lt = []

while True:
	txt = input()
	if txt != '':
		for i in txt:
			tp.append(txt.count(i))
		lt.append(tp)
		tp = []
	else:
		break

print(lt)