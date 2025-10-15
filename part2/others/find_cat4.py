n = int(input())
cat = False

for x in range(n):
	y = input()
	if ('Кот' in y or 'кот' in y) and not ('Пёс' in y or 'пёс' in y):
		cat = True
	elif (('Пёс' in y or 'пёс' in y) and ('Кот' in y or 'кот' in y)):
		cat = False
	elif 'Пёс' in y or 'пёс' in y:
		cat = False

if cat:
	print('МЯУ')
else:
	print('НЕТ')