'''x = 0
good = 0
good1 = 0
bad = 0
bad1 = 0

while True:
	if x != '':
		x = input()
		if x == 'добрый':
			good += 1
			good1 += good
		elif x == 'злой':
			bad += 1
			bad1 += bad
		elif x == 'Какой подарок?':
			good = 0
			bad = 0
	else:
		break

if good > bad and x == 'добрый':
	print('серебряный шиллинг')
elif good < bad and x == 'злой':
	print('золотой')
elif (good < bad and x != 'злой') or (good > bad and x != 'добрый'):
	if good1 > bad1 and x == 'добрый':
		print('серебряный шиллинг')
	elif good1 < bad1 and x == 'злой':
		print('золотой')

print('Ах, не знаю!')'''




last = ''
evil = 0
good = 0

while (letter := input()) != '':
	if letter == 'Какой подарок?':
		if good > evil and last == 'добрый':
			print('серебряный шиллинг')
		elif good < evil and last == 'злой':
			print('золотой шиллинг')
		else:
			print('Ах, не знаю!')
			break
		evil = 0
		good = 0
	elif letter == 'добрый':
		last = 'добрый'
		good += 1
	elif letter == 'злой':
		last = 'злой'
		evil += 1