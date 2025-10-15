from math import prod


def multiplier(*nums, key):
	lt = list(filter(key, nums))
	if lt != []:
		new = prod(lt)
		return new
	return None

print(multiplier(2, 3, 4, 5, key=lambda x: x % 2))