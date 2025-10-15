m = int(input())
grass_list = set()

for x in range(m):
	i = int(input())
	for y in range(i):
		grass = input()
		grass_list.add(grass)

for n in grass_list:
	print(n)