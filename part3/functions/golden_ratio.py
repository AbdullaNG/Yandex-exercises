def golden_ratio(i):
	count = 0
	x1 = 0
	x2 = 1
	while True:
		x3 = x1 + x2
		x1 = x2
		x2 = x3
		count += 1
		if count == i:
			print(x3 / x1)
			break

