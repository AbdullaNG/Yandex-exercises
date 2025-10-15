n = int(input())
texts = []

for i in range(n):
	txt = input()
	texts.append(txt)

for x in range(len(texts)):
	for y in range(len(texts)):
		if len(texts[x]) < len(texts[y]):
			texts[x], texts[y] = texts[y], texts[x]
		elif len(texts[x]) == len(texts[y]):
			if texts[x] < texts[y]:
				texts[x], texts[y] = texts[y], texts[x]

for z in texts:
	print(z)