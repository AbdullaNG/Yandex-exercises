bd = {
			'янв': [], 'фев': [], 'мар': [], 'апр': [], 'май': [], 'июн': [],
			'июл': [], 'авг': [], 'сен': [], 'окт': [], 'ноя': [], 'дек': []
}
n = int(input())

for i in range(n):
	txt = input().split()
	name = txt[0]
	month = txt[2]
	bd[month].append(name)
	bd[month].sort()

m = int(input())

for j in range(m):
	mt = input()
	print(' '.join(bd[mt]))