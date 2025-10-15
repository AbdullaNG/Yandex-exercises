def fractal_print(obj):
	lt = []
	lt.extend(obj[:len(obj) // 2])
	lt.extend(obj[len(obj) // 2:])
	print(lt)