class BigBell:
	c = 0

	def sound(self):
		if self.c % 2 == 0:
			print('ding')
		else:
			print('dong')
		self.c += 1