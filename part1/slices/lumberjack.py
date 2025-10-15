txt = input()
n = int(input())
flag = True

while len(txt) > n:
	if flag:
		print(txt[-1 * n:])
		txt = txt[:-1 * n]
		flag = False
	else:
		print(txt[:n])
		txt = txt[n:]
		flag = True
if txt:
	print(txt)