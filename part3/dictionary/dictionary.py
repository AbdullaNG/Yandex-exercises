n = int(input())
d = {}

for i in range(n):
	txt = input().split(' ')
	x = txt.pop(0)
	d[x] = ' '.join(txt)

m = int(input())

for j in range(m):
	key = input()
	if key in d:
		print(d[key])
	else:
		print('Нет в словаре')