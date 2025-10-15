x = int(input())
things = set()

for i in range(x):
	thing = input()
	things.add(thing)

y = int(input())
ing = set()

for n in range(y):
	recipe = input()
	ingredients = int(input())
	flag = True
	for z in range(ingredients):
		ingredient = input()
		ing.add(ingredient)
	for s in ing:
		if s not in things:
			flag = False
	if flag:
		print(recipe)
	ing = set()