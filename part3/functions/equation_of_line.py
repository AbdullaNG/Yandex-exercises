def equation(a, b):
	a = [float(i) for i in a.split(';')]
	b = [float(j) for j in b.split(';')]
	if a[0] == b[0]:
		print(a[0])
	elif a[1] == b[1]:
		print(a[1])
	else:
		k = (a[1] - b[1]) / (a[0] - b[0])
		b = b[1] - k * b[0]
		print(k, b)