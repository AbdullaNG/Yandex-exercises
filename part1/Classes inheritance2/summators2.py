class Summator:
	def transform(self):
		pass

	def sum(self, N):
		return N * (N + 1) / 2


class PowerSummator(Summator):
	def __init__(self, b):
		self.b = b

	def transform(self):
		pass

	def sum(self, N):
		return sum([i ** self.b for i in range(N + 1)])


class SquareSummator(PowerSummator):
	def __init__(self, b):
		pass

	def transform(self):
		pass

	def sum(self, N):
		return N * (N + 1) * (2 * N + 1) / 6


class CubeSummator(PowerSummator):
	def __init__(self, b):
		pass

	def transform(self):
		pass

	def sum(self, N):
		return (N * (N + 1) / 2) ** 2