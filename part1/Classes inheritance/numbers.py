class NaturalNumber:
	def __init__(self, n):
		self.n = n
	
	def __str__(self):
		return f'{self.__class__.__name__}({self.n})'
	
	def __add__(self, other):
		if self.n + other.n > 0:
			return NaturalNumber(self.n + other.n)
		return NaturalNumber(None)
	
	def __sub__(self, other):
		if self.n - other.n > 0:
			return NaturalNumber(self.n - other.n)
		return NaturalNumber(None)


class Integer(NaturalNumber):
	def __add__(self, other):
		return Integer(self.n + other.n)
	
	def __sub__(self, other):
		return Integer(self.n - other.n)


class RealNumber(Integer):
	def __add__(self, other):
		return RealNumber(self.n + other.n)
	
	def __sub__(self, other):
		return RealNumber(self.n - other.n)


class ComplexNumber(RealNumber):
	def __add__(self, other):
		return ComplexNumber(self.n + other.n)
	
	def __sub__(self, other):
		return ComplexNumber(self.n - other.n)


nn = NaturalNumber(8)
nn1 = NaturalNumber(10)
print(nn + nn1, nn - nn1)
print(nn1 + nn, nn1 - nn)
it = Integer(7)
it1 = Integer(-5)
print(it - it1, it + it1)
print(it - nn, nn - it)
print(it + nn1, nn1 + it)
rn = RealNumber(9.0)
rn1 = RealNumber(-5.6)
print(rn - rn1, rn1 + rn)
print(nn - rn, rn1 + nn1)
cn = ComplexNumber((5+3j))
cn1 = ComplexNumber((-1-1.3j))
print(cn - cn1, cn + cn1)
print(nn + cn, cn1 - it)