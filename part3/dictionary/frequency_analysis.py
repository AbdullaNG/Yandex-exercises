n = int(input())
lt = []
st = set()
invd = ',.!?:;'
tp = []
last = []
c = 0

for i in range(n):
	txt = input()
	new = ''
	for j in txt:
		if j in invd:
			continue
		else:
			new += j
	new = [a.capitalize() for a in new.lower().split()]
	lt.extend(new)

for z in lt:
	st.add((lt.count(z), z))

st = list(st)
st.sort(reverse=True)

if len(st) > 2:
	k = st[0]
	for x in st[1:]:
		c += 1
		if x[0] == k[0]:
			tp.append(k[1])
			if c == len(st) - 1:
				tp.append(x[1])
				tp.sort()
				last.extend(tp)
		else:
			tp.append(k[1])
			tp.sort()
			last.extend(tp)
			tp = []
		k = x

	for abc in last:
		print(abc)
else:
	for m in st:
		print(m[1])