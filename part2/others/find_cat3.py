cat = False
count = 1
y = ''
catnum = 0

while y != 'СТОП':
	y = input()
	if 'Кот' in y or 'кот' in y:
		cat = True
		catnum += 1
	if not cat:
		count += 1

if cat:
	print(catnum, count)
else:
	print(catnum, -1)