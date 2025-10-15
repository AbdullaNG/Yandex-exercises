word = input()
ln = len(word)
c = ln // 2
spc = -1

if ln % 2 != 0:
	print(' ' * (ln // 2) + word[ln // 2] + ' ' * (ln // 2))
	ln -= 2

	while True:
		if ln <= 0:
			break
		c += 1
		spc += 2
		print(' ' * (ln // 2) + word[ln // 2] + ' ' * spc + word[c])
		ln -= 2
else:
	print(' ' * (ln // 2 - 1) + word[ln // 2 - 1:ln // 2 + 1] + ' ' * (ln // 2))
	ln -= 3
	spc = 0

	while True:
		if ln <= 0:
			break
		c += 1
		spc += 2
		print(' ' * (ln // 2) + word[ln // 2] + ' ' * spc + word[c])
		ln -= 2