n = int(input())
check = input()
x = 0

for i in range(n):
	txt = input()
	if 'забыл' in txt or check in txt:
		x += 1

if x < n / 2:
	print('НЕ ТАК И МНОГО')
	print(n + x)
else:
	print('ВСЕ РАВНО НИЧЕГО СТРАШНОГО')
	print(n + x)
#------------------------EASY--------------------------