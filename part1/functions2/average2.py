def average(values):
	if values != []:
		s = 0
		for i in values:
			s += i
		return s / len(values)
	return 0