def template(a, b, c):
	if a + b > c and a + c > b and c + b > a:
		s = a + b + c
		print('Периметр:', s)
		area = (s / 2) * (s / 2 - a) * (s / 2 - b) * (s / 2 - c)
		print('Площадь:', area ** 0.5)
		print('Равнобедренный: да' if a == b or a == c or b == c else 'Равнобедренный: нет')
		print('Равносторонний: да' if a == b == c else 'Равносторонний: нет')
	else:
		print('None')