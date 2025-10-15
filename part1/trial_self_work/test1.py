txt = ''
texts = []
summ = 0

while 'Гэндальф' not in txt:
	txt = input()
	if 'волшебн' in txt:
		texts.append(txt)

for i in texts:
	summ += len(i)

print(summ)
#------------------------EASY--------------------------