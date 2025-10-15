num = int(input())
over = set()
even = set()
multiple3 = set()

for x in range(num):
	legs = int(input())
	if legs > 40:
		over.add(legs)
	elif legs % 2 == 0:
		even.add(legs)
	elif legs % 3 == 0:
		multiple3.add(legs)

for x in over:
	if x % 3 == 0 and x % 2 == 0:
		continue
	elif x % 3 == 0 or x % 2 == 0:
		print(x, end=' ')

for x in even:
	if x % 3 == 0 and x > 40:
		continue
	elif x % 3 == 0 or x > 40:
		print(x, end=' ')

for x in multiple3:
	if x > 40 and x % 2 == 0:
		continue
	elif x > 40 or x % 2 == 0:
		print(x, end=' ')