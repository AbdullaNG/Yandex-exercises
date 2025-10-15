n = int(input())
phonebook = {}

for i in range(n):
	info = input().split()
	if info[1] not in phonebook:
		phonebook[info[1]] = info[0]
	else:
		phonebook[info[1]] += ' ' + info[0]

m = int(input())

for j in range(m):
	name = input()
	if name in phonebook:
		print(phonebook[name])
	else:
		print('Нет в телефонной книге')