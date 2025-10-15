n = int(input())
lt = []
x = 0
o = 0
flag = False
flag1 = False

for i in range(n):
	txt = input()
	lt.append(txt)

for j in lt:
	if 'xxx' in j:
		print('x')
		flag = False
		flag1 = True
		break
	elif 'ooo' in j:
		print('o')
		flag = False
		flag1 = True
		break

if flag1 is False:
	for y in range(n):
		for z in lt:
			if z[y] == 'x':
				o = 0
				x += 1
				if x >= 3:
					break
			elif z[y] == 'o':
				x = 0
				o += 1
				if o >= 3:
					break
			else:
				x = 0
				o = 0
		if x >= 3:
			print('x')
			flag = False
			break
		elif o >= 3:
			print('o')
			flag = False
			break
		else:
			flag = True
		x = 0
		o = 0

if flag:
	print('-')