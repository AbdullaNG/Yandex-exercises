def divide(num):
	b1 = num % 10
	b2 = num % 100 // 10
	b3 = num % 1000 // 100
	b4 = num % 10000 // 1000
	b5 = num % 100000 // 10000
	b6 = num % 1000000 // 100000
	s1 = b1 + b2 + b3
	s2 = b4 + b5 + b6
	if s1 == s2:
		return True
	return False


def lucky(ticket):
	flag1 = divide(ticket)
	flag2 = divide(lastTicket)
	if flag1 == flag2 == True:
		return 'Счастливый'
	return 'Несчастливый'

lastTicket = 100001
print(lucky(101))