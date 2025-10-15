n = int(input())
whitelist = []

for i in range(n):
	white = input()
	whitelist.append(white)

m = int(input())
search = []

for j in range(m):
	srch = input()
	search.append(srch)

for x in search:
	if x in whitelist:
		print(x)