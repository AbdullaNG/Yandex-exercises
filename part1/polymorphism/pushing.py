import math


class Square:
	def __init__(self, a):
		self.a = a
	
	def extrude(self, h):
		return self.a ** 2 * h


class Rectangle:
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def extrude(self, h):
		return self.a * self.b * h


class Triangle:
	def __init__(self, a):
		self.a = a
	
	def extrude(self, h):
		return 3 ** (1 / 2) * self.a ** 2 / 4 * h


class Circle:
	def __init__(self, a):
		self.a = a
	
	def extrude(self, h):
		return self.a ** 2 * math.pi * h


sq = Square(1)
rec = Rectangle(1, 2)
tr = Triangle(1)
cir = Circle(1)
for item in (sq, rec, tr, cir):
    print(item.extrude(1))