n = int(input())

for i in range(n):
	txt = input()
	if txt[:3] == 'не ' or txt[:3] == 'Не ':
		print(txt[3:])
	else:
		print(txt)