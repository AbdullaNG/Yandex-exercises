def ask_password():
	flag = False
	for i in range(3):
		password = input()
		if password == 'password':
			print('Пароль принят')
			flag = True
			break
	if flag is False:
		print('В доступе отказано')