n = int(input())
stop = False
for i in range(1, n):
	if i == 2 or i == 3:
		print(i)
	for j in range(2, int((i / 2) + 1)):
		if i % j != 0: 
			stop = True
		else:
			stop = False
			break
	if stop == True:
		print(i)