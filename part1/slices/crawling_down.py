ctrl = input()
sym = ""
x = 1
poss = 0

while x < len(ctrl):
	if ctrl[x] == 'V':
		if ctrl[0] == ' ':
			z = 'V'
		else:
			z = ctrl[0]
		print(sym[:poss] + z + sym[(poss + 1):])
		sym = ' ' * poss
	elif ctrl[x] == '>':
		if ctrl[0] == ' ':
			z = '>'
		else:
			z = ctrl[0]
		sym += z
		poss += 1
	elif ctrl[x] == '<':
		if ctrl[0] == ' ':
			z = '<'
		else:
			z = ctrl[0]
		sym = sym[:poss] + z + sym[(poss + 1):]
		poss -= 1
		if poss < 0:
			break
	x += 1

if poss >= 0:
	if sym != '':
		if ctrl[0] == ' ':
			z = ''
		else:
			z = ctrl[0]
		print(sym[:poss] + z + sym[(poss + 1):])
	else:
		print(ctrl[0])
else:
	print(sym)