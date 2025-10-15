n = int(input())
milks = [int(input()) for i in range(n)]
minn = int(input())
maxx = int(input())

for j in milks:
	if j >= minn and j <= maxx:
		print(j)