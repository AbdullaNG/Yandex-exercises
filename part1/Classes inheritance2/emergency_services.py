class Service:
	def __init__(self, address, id):
		self.address = address
		self.id = id
	
	def arrival_time(self):
		return len(self.address)
	
	def get(self):
		d = {'address': self.address, 'id': self.id}
		return d


class Ambulance(Service):
	def __init__(self, address, id, mode, severity):
		super().__init__(address, id)
		self.mode = mode
		self.severity = severity
	
	def get(self):
		d = super().get()
		d['mode'] = self.mode
		d['severity'] = self.severity
		return d


class Firefighters(Service):
	def __init__(self, address, id, mode, victims):
		super().__init__(address, id)
		self.mode = mode
		self.victims = victims
	
	def get(self):
		d = super().get()
		d['mode'] = self.mode
		d['victims'] = self.victims
		return d


class Police(Service):
	def __init__(self, address, id, mode, victims, armament_required):
		super().__init__(address, id)
		self.mode = mode
		self.victims = victims
		self.armament_required = armament_required
	
	def get(self):
		d = super().get()
		d['mode'] = self.mode
		d['victims'] = self.victims
		d['armament_required'] = self.armament_required
		return d

pol = Police("Tverskaya St., 13, Moscow, Russia", 3, 1, 0, False)
print(pol.get())
print(pol.arrival_time())