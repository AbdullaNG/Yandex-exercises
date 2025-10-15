class Summator:
	def transform(self):
		pass

	def sum(self, N):
		return N * (N + 1) / 2


class SquareSummator(Summator):
	def transform(self):
		pass

	def sum(self, N):
		return N * (N + 1) * (2 * N + 1) / 6


class CubeSummator(Summator):
	def transform(self):
		pass

	def sum(self, N):
		return (N * (N + 1) / 2) ** 2