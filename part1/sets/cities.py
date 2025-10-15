n = int(input())
cities = set()

for x in range(n):
	city = input()
	cities.add(city)

city = input()

if city in cities:
	print('TRY ANOTHER')
else:
	print('OK')