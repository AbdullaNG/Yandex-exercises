def tic_tac_toe(field):
	o = 0
	x = 0
	flag = True
	fg = True
	for i in field:
		if ''.join(i) == '000':
			print('0 win')
			flag = False
			break
		elif ''.join(i) == 'xxx':
			print('x win')
			flag = False
			break

	if flag:
		for y in range(3):
			for z in field:
				if z[y] == 'x':
					o = 0
					x += 1
					if x == 3:
						print('x win')
						fg = False
						break
				elif z[y] == '0':
					x = 0
					o += 1
					if o == 3:
						print('0 win')
						fg = False
						break
				else:
					x = 0
					o = 0
			x = 0
			o = 0

		if x < 3 and o < 3 and fg:
			if field[0][0] + field[1][1] + field[2][2] == 'xxx':
				print('x win')
			elif field[0][0] + field[1][1] + field[2][2] == '000':
				print('0 win')
			elif field[0][2] + field[1][1] + field[2][0] == '000':
				print('0 win')
			elif field[0][2] + field[1][1] + field[2][0] == '000':
				print('x win')
			else:
				print('draw')



data="""x 0 -
x - 0
x 0 -"""

field = [line.split() for line in data.split('\n')]
tic_tac_toe(field)