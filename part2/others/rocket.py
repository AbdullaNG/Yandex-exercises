n = int(input())

for x in range(1, n + 1):
	for y in range(x, 0, -1):
		print('Осталось секунд:', y - 1)
	print('Пуск', x)