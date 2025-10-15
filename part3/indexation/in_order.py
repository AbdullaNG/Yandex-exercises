text = input()
index1 = ord(text[0])
flag = False

for i in range(1, len(text)):
	if index1 < ord(text[i]):
		flag = True
	else:
		print(text[i])
		flag = False
		break
	index1 = ord(text[i])

if flag:
	print('(:_0_:)')