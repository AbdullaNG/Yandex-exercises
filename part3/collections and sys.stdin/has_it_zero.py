import sys


data = [i.strip('\n') for i in sys.stdin.readlines()]
lt = []
for j in data:
	lt.append(all(a != 0 for a in [int(x) for x in j.split()]))

if False in lt:
	print(True)
else:
	print(False)