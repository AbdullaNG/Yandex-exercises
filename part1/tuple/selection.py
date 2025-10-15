n = int(input())
list1 = []

for i in range(n):
	txt = input()
	list1.append(txt)
	print(txt)
print()

for j in list1:
	if '2' in j or '3' in j or '1' in j:
		continue
	else:
		print(j)