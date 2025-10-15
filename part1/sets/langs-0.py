N = int(input())
M = int(input())
nset = set()
mset = set()
for n in range(N):
	eng = input()
	nset.add(eng)
for m in range(M):
	ger = input()
	mset.add(ger)
not_both = nset.symmetric_difference(mset)
if not_both:
	print(len(not_both))
else:
	print('NO')