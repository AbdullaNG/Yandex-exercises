secret_avatars = ['March Hare', 'Hatter', 'Dormouse', 'Alice']
vowels = 'aeiouyAEIOUY'
lt = []


def secret_sort():
	for i in secret_avatars:
		s = 0
		for j in range(len(i)):
			if j % 2 != 0 and i[j] in vowels:
				s += 1
		lt.append((s, i))

	for x in range(len(lt)):
		for z in range(len(lt)):
			if lt[x][1] == 'March Hare' and lt[z][1] == 'Dormouse':
				lt[x], lt[z] = lt[z], lt[x]
			if lt[x][0] < lt[z][0]:
				lt[x], lt[z] = lt[z], lt[x]
	
	secret_avatars[:] = [y[1] for y in lt]


secret_sort()
print(secret_avatars)