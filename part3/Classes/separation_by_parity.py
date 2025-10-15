class OddEvenSeparator:
	def __init__(self):
		self.lt = []

	def add_number(self, n):
		self.lt.append(n)
	
	def odd(self):
		return [i for i in self.lt if i % 2 != 0]
	
	def even(self):
		return [i for i in self.lt if i % 2 == 0]



sep1 = OddEvenSeparator()
sep2 = OddEvenSeparator()
for i in range(50):
    if i % 2 == 0:
        sep1.add_number(i)
    else:
        sep2.add_number(i)

print(' '.join(map(str, sep1.even())))
print(' '.join(map(str, sep1.odd())))

print(' '.join(map(str, sep2.even())))
print(' '.join(map(str, sep2.odd())))