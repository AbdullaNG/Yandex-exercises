from math import radians, sin
ALPHA = 45
L = 10
g = 9.8
def collect_stones():
	global L
	v = (g * L / sin(2 * radians(ALPHA))) ** 0.5
	L += 0.5
	return v