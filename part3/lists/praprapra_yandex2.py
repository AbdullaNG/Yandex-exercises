n = int(input())
listt = []
search_list = []
flag = False

for i in range(n):
	txt = input()
	listt.append(txt)

search_num = int(input())
for x in range(search_num):
	search = input()
	search_list.append(search)
     
for j in listt:
	for y in search_list:
		if y in j:
			flag = True
		else:
			flag = False
			break
	if flag:
		print(j)