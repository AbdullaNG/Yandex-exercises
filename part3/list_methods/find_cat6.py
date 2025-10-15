n = int(input())
texts = [input() for i in range(n)]
final = [f'{texts.index(x) + 1} {x.find('кот') + 1}' for x in texts if x.find('кот') != -1]
for y in final:
	print(y)