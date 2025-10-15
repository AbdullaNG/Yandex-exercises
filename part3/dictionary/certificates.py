n = int(input())
cert = {}

for i in range(n):
	txt = input().split()
	cert[txt[0]] = ' '.join(txt[1:])

score = sum([int(j) for j in input().split()])

for x in cert:
	if score >= int(cert[x].split()[0]) and score <= int(cert[x].split()[1]):
		print(x)