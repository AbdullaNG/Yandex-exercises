def print_statistics(arr):
	arr.sort()
	print(len(arr))

	if len(arr) != 0:
		print(sum(arr) / len(arr))
		print(min(arr))
		print(max(arr))

		x = len(arr)
		if x % 2 == 0:
			median = (arr[int(x / 2) - 1] + arr[int(x / 2 + 1) - 1]) / 2
		else:
			median = arr[int((x + 1) / 2) - 1]
		print(median)
	else:
		print(0, 0, 0, 0, sep='\n')