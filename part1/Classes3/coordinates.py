class Point:
	def __init__(self, x, y):
		self.xy = (x, y)
	
	def __eq__(self, other):
		return self.xy == other.xy


p1 = Point(0, 10)
p2 = Point(0, 0)

if p1 == p2:
    print("Equal True")
else:
    print("Equal False")

if p1 != p2:
    print("Not equal True")
else:
    print("Not equal False")
