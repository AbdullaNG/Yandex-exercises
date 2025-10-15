forr = 0
against = 0


def voting(choice):
	global forr
	global against
	if choice == 'за':
		forr += 1
	else:
		against += 1
	print(f'за: {forr}')
	print(f'против: {against}')
	print()