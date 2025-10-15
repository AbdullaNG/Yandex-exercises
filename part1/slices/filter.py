n = int(input())

for i in range(n):
	txt = input()
	if txt[:4] == '####':
		continue
	elif txt[:2] == '%%':
		print(txt[2:])
	else:
		print(txt)