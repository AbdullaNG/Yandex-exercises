m = int(input())
meal_list = set()

for x in range(m):
	new_meal = input()
	meal_list.add(new_meal)

n = int(input())

for y in range(n):
	i = int(input())
	for z in range(i):
		cooked_meal = input()
		meal_list.discard(cooked_meal)

for last_meal in meal_list:
	print(last_meal)