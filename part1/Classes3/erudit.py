class Scrabble:
	def __init__(self, word):
		self.word = word
		self.points = 0
		for x in self.word:
			if x in 'AEILNORSTU':
				self.points += 1
			elif x in 'DG':
				self.points += 2
			elif x in 'BCMP':
				self.points += 3
			elif x in 'FHVWY':
				self.points += 4
			elif x in 'K':
				self.points += 5
			elif x in 'JX':
				self.points += 8
			elif x in 'QZ':
				self.points += 10
		self.len = len(self.word)
	
	def __str__(self):
		return f'Scrabble(\'{self.word}\')'
	
	def __call__(self, current_word):
		score = 0
		flag = True
		for i in current_word:
			if i not in self.word:
				flag = False
				break
		for z in current_word:
			if current_word.count(z) > self.word.count(z):
				flag = False
				break
		if flag:
			for j in current_word:
				if j in 'AEILNORSTU':
					score += 1
				elif j in 'DG':
					score += 2
				elif j in 'BCMP':
					score += 3
				elif j in 'FHVWY':
					score += 4
				elif j in 'K':
					score += 5
				elif j in 'JX':
					score += 8
				elif j in 'QZ':
					score += 10
			return score
		return score
	
	def __eq__(self, other):
		return self.len == other.len
	
	def __ne__(self, other):
		return self.len != other.len
	
	def __lt__(self, other):
		return self.len < other.len
	
	def __gt__(self, other):
		return self.len > other.len
	
	def __le__(self, other):
		return self.len <= other.len
	
	def __ge__(self, other):
		return self.len >= other.len


sc = Scrabble('COMPUTER')
sc1 = Scrabble('TROLLEYBUS')
print(sc('COMPUTE'))
print(sc('METRO'))
print(sc('TERMITE'))
print(sc1('OUSTER'))
print(sc1('BOTTLE'))
print(sc1('TROUBLE'))
print(sc > sc1, sc <= sc1, sc != sc1, sc >= sc1, sc == sc1, sc > sc1)