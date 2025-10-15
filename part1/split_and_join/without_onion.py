n = int(input())
recipe = []

for i in range(n):
	txt = input()
	if 'лук' not in txt:
		recipe.append(txt)

print(', '.join(recipe))