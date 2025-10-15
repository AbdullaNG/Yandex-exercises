def hello(name):
	print(f'Здравствуйте, {name}! Вашу карту ищут...')


def search_card(name):
	if name in base:
		print(f'Ваша карта с номером {base.index(name) + 1} найдена')
	else:
		print('Ваша карта не найдена')


base = []