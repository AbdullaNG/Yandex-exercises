list1 = []
lt = []
s = 0
new = []

while True:
	txt = input()
	list1.append(txt)
	if txt == '':
		break
	else:
		lt.append(txt[0])
		lt.append(txt[1])

for i in lt:
	if i not in new:
		s += 1
	new.append(i)

lt = set(lt)
lt = list(lt)
lt.sort()

print(end='  ')
for z in lt:
	print(z, end=' ')
print()

for x in range(s):
	print(lt[x], end=' ')
	for y in lt:
		if lt[x] + y in list1:
			print(1, end=' ')
		else:
			print(0, end=' ')
	print()