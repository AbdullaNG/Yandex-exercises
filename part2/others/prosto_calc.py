op = ''

while op != 'x':
	num1 = int(input())
	op = input()
	if op != '!' and op != 'x':
		num2 = int(input())
	elif op == '!':
		fac = 1
		if num1 >= 0:
			for i in range(1, num1 + 1):
				fac *= i
			print(fac)
	if op == '+':
		print(num1 + num2)
	elif op == '-':
		print(num1 - num2)
	elif op == '*':
		print(num1 * num2)
	elif op == '/' and num2 != 0:
		print(num1 // num2)
	elif op == '%' and num2 != 0:
		print(num1 % num2)
	elif op == 'x':
		print(num1)
		break