import string
import random


def generate_password(m):
	lt = ''
	new = ''
	bad = 'Il10oO'
	sym = string.ascii_letters + string.digits
	n = 0
	for i in sym:
		if i in bad:
			continue
		else:
			new += i
	while True:
		pswd = random.choice(new)
		if pswd not in lt:
			lt += pswd
			n += 1
		if n == m:
			return lt


def main(n, m):
	tp = []
	count = 0
	while True:
		c = generate_password(m)
		if c not in tp:
			tp.append(c)
			count += 1
		if count == n:
			return tp