txt = input()
maxx = txt
minn = txt
flag = True

while True:
	txt = input()
	if txt == 'стоп':
		break

	if len(txt) > len(maxx):
		maxx = txt
	elif len(txt) < len(minn):
		minn = txt

for i in minn:
	if i not in maxx:
		flag = False

if flag:
	print('ДА')
else:
	print('НЕТ')