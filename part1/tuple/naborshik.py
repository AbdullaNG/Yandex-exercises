txt = input()
x = []
eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"'
ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
count = 0
set1 = set()

for i in txt:
	if i in eng:
		for x in eng:
			count += 1
			if x == i:
				set1.add((i, count))
		count = 0
	elif i in ru:
		for x in ru:
			count += 1
			if x == i:
				set1.add((i, count))
		count = 0

for s in set1:
	print(s)