num = int(input())
doska_num = 0
text = ''

while text != 'КОНЕЦ':
	text = input()
	if 'доска' in text or 'дощечка' in text:
		doska_num += 1
		print(f'Прибили {doska_num} дощечку.')
	if doska_num == num:
		print('ГОТОВО')
		break
if doska_num != num:
		print('МАЛОВАТО')