import sys


data = [i.strip('\n') for i in sys.stdin.readlines()]
lt = []
lt1 = []

for j in data:
	lt.append(list(filter(lambda a: a.isdigit(), j.split())))

high = max([len(x) for x in lt])
lt = list(filter(lambda b: len(b) == high, lt))
for m in lt:
	lt1.append(sum([int(k) for k in m]))

print(min(lt1) if min(lt1) != 0 else -1)