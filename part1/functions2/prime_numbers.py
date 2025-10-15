def prime(number):
	flag = True
	for i in range(2, number):
		if number % i == 0:
			flag = False
	if flag:
		return 'Простое число'
	return 'Составное число'