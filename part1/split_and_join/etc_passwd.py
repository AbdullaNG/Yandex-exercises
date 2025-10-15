texts = []

while True:
	txt = input()
	if txt == '':
		break
	texts.append(txt.split(':'))

pswd = input().split(';')

for i in texts:
	if i[1] in pswd:
		print('To:', i[0])
		print(i[4].split(',')[0] + ',', 'ваш пароль слишком простой, смените его.')