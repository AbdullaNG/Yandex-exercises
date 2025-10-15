x = 0
y = 0
bus_stations1 = set()
bus_stations2 = set()

while True:
	if x == '':
		break
	else:
		x = input()
		if x != '':
			bus_stations1.add(x)

while True:
	if y == '':
		break
	else:
		y = input()
		if y != '':
			bus_stations2.add(y)
		if y in bus_stations1:
			print(y)

both = bus_stations2.intersection(bus_stations1)
if both == set():
	print('EMPTY')