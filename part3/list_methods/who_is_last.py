n = int(input())
lt = []

for i in range(n):
	txt = input()
	if txt[0] == 'Я':
		lt.insert(0, txt[23:-1])
	elif txt == 'Следующий!' and lt != []:
		print(f'Заходит {lt.pop(0)}!')
	elif txt == 'Следующий!' and lt == []:
		print('В очереди никого нет.')
	else:
		lt.append(txt[19:-1])