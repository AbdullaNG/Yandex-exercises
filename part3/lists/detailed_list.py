n = int(input())
detailed_list = []

for i in range(n):
	txt = input()
	count = input()
	x = str(txt + ' ' + count)
	detailed_list.append(x)

for j in detailed_list[::-1]:
	print(j)