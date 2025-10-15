n = int(input())
tp = []
st = set()

for i in range(n):
	num = int(input())
	tp.append(num)

for j in tp:
	for x in tp:
		st.add(j - x)

lt = list(st)
lt.sort()

for y in lt:
	print(y)