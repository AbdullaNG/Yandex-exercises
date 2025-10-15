class User:
	def __init__(self, name):
		self.name = name
	
	def send_message(self, user, message):
		return f'For {user}: message:{message}'
	
	def post(self, message):
		pass

	def info(self):
		return ''
	
	def describe(self):
		print(self.name, self.info())


class Person(User):
	def __init__(self, name, birthdate):
		self.name = name
		self.birthdate = birthdate
	
	def info(self):
		return f'Дата рождения:{self.birthdate}'
	
	def subscribe(self, user):
		pass


class Community(User):
	def __init__(self, name, info):
		self.name = name
		self.inf = info
	
	def info(self):
		return f'Описание: {self.inf}'