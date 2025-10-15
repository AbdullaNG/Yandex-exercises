scoring = {'Яблочко': 50, 'Зеленое_кольцо': 25,
'Внешнее_кольцо': {1: 8, 2: 6, 3: 42, 20: 50},
'Внутреннее_кольцо': {1: 2, 2: 16, 3: 56, 20: 3}}


def score(x, y=0):
	global scoring
	if not y:
		if x == 'Яблочко':
			return 50
		elif x == 'Зеленое_кольцо':
			return 25
	else:
		if x == 'Внешнее_кольцо':
			return scoring[x][int(y)]
		elif x == 'Внутреннее_кольцо':
			return scoring[x][int(y)]


print(score('Зеленое_кольцо'))