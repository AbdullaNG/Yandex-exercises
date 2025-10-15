class Rainbow:
	def __init__(self, n=1):
		self.n = n
	
	colors = ['red', 'orange', 'yellow', 'green', 'light blue', 'blue', 'violet']

	def next_color(self, color):
		if self.n == 1 or self.n == 3:
			if self.colors.index(color) < 6:
				return self.colors[self.colors.index(color) + 1]
			return self.colors[0]
		return self.colors[self.colors.index(color) - 1]