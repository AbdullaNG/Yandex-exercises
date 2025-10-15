class Wardrobe:
	def __init__(self, *things):
		self.things = list(things)
	
	def __str__(self):
		return ' '.join(self.things)


class JustWardrobe(Wardrobe):
	def __str__(self):
		self.things[0] = self.things[0].capitalize()
		return ', '.join(self.things) + '.'


class MagicWardrobe(Wardrobe):
	def __str__(self):
		self.things.sort()
		return ', '.join(self.things) + '.'


wa = Wardrobe("socks", "jacket", "hat")
jw = JustWardrobe("trousers", "blouse")
mw = MagicWardrobe("Narnia", "Wonderland", "Dreamland")
print(*[wa, jw, mw], sep='\n')