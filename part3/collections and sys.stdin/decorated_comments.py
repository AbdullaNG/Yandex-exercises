import sys


data = [i.strip('\n') for i in sys.stdin.readlines()]
c = 0
for j in data:
	c += 1
	if j.strip()[0] == '#':
		if j.strip()[1] == ' ':
			print(f'Line {c}:{j.strip()[1:]}')
		else:
			print(f'Line {c}: {j.strip()[1:]}')