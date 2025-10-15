class Balance:
	l, r = 0, 0

	def add_left(self, n):
		self.l += n
	
	def add_right(self, n):
		self.r += n
	
	def result(self):
		if self.l > self.r:
			return 'L'
		elif self.l < self.r:
			return 'R'
		return '='