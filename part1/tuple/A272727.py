n = int(input())
lt = [0]

for i in range(n):
	lt1 = 0
	for j in range(len(lt)):
		if lt[j] == lt[-1 - j]:
			lt1 += 1
	lt.append(lt1)

del lt[-1]

for x in lt:
	print(x)