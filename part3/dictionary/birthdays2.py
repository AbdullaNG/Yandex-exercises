bd = {
	'янв': [],
	'фев': [],
	'мар': [],
	'апр': [],
	'май': [],
	'июн': [],
	'июл': [],
	'авг': [],
	'сен': [],
	'окт': [],
	'ноя': [],
	'дек': [],
}
n = int(input())

for i in range(n):
	txt = input().split(' ')
	bd[txt[2]] += [[int(txt[1]), txt[0]]]

for j in bd:
	bd[j].sort()
	j1 = []
	for z in bd[j]:
		z.reverse()
		j1 += z
	bd[j] = j1

m = int(input())

for x in range(m):
	mt = input()
	if len(bd[mt]) == 0:
		print()
	else:
		for b in range(len(bd[mt])):
			if b < len(bd[mt]) - 1:
				print(bd[mt][b], end=' ')
			else:
				print(bd[mt][b])