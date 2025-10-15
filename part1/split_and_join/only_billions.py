txt = input()
txt1 = ''
count = 0

for i in txt:
	count += 1
	if i == ';':
		z = [j for j in txt1.split(',') if int(j) >= 1000000000]
		print(','.join(z))
		txt1 = ''
		z = []
		continue
	txt1 += i
	if count == len(txt):
		z = [j for j in txt1.split(',') if int(j) >= 1000000000]
		print(','.join(z))