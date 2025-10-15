import sys


data = [i.strip('\n') for i in sys.stdin.readlines()]
c = 0
for j in data:
	if j != '':
		if j.strip()[0] == '#':
			c += 1
print(c)