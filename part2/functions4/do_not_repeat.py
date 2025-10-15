divisors = {}


def number_of_divisors(n):
	s = 0
	if n not in divisors.keys():
		for i in range(1, int(n ** 0.5) + 1):
			if n % i == 0:
				s += 1
				if i != n // i:
					s += 1
		divisors[n] = s
		return s
	return divisors[n]