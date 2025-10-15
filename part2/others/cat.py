cat = False
count = 1
y = ''

while y != 'СТОП':
	y = input()
	if 'Кот' in y or 'кот' in y:
		cat = True
		break
	if not cat:
		count += 1

if cat:
	print(count)
else:
	print(-1)


'''cat = False
n = int(input())

for x in range(n):
	y = input()
	if 'Кот' in y or 'кот' in y:
		cat = True
		break

if cat:
	print('МЯУ')
else:
	print('НЕТ')'''