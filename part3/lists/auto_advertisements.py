n1 = int(input())
ad_list = []

for i in range(n1):
	ad = input()
	ad_list.append(ad)

n2 = int(input())
for j in range(n2):
	num = int(input())
	print(ad_list[num - 1])