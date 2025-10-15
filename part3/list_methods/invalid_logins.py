logins = input().split(',')
corr = 'йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm_1234567890'
flag = False
bad = []

for i in logins:
	for j in i.lower():
		if j not in corr:
			flag = True
			break
	if flag:
		bad.append(i)
	flag = False

if bad != []:
	bad.sort()
	maxx = max([len(z) for z in bad])

	for y in bad:
		print(' ' * (maxx - len(y)) + y)