import sys


data = [i.strip('\n') for i in sys.stdin.readlines()]
lt = []
for j in data:
	lt.append(all(a % 5 != 0 for a in [int(x) for x in j.split('; ')]))

print('OK' if any(lt) else 'FAIL')