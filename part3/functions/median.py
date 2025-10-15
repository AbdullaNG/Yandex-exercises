def median(data):
	data.sort()
	x = len(data)
	if x % 2 == 0:
		median = (data[int(x / 2) - 1] + data[int(x / 2 + 1) - 1]) / 2
	else:
		median = data[int((x + 1) / 2) - 1]
	print(median)