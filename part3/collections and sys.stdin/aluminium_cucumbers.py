import sys


data = sys.stdin.readlines()
data = [i.strip('\n').split() for i in data]
lt = []

for j in data:
	t = 0
	c = 0
	for x in j:
		if '0' in x:
			c += 1
		else:
			t += 1
	lt.append(True if t >= c else False)

print('EVERGREEN TOMATOES' if all(lt) else 'ALUMINUM CUCUMBERS')