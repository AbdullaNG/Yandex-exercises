n = int(input())
z = 0
for x in range(1, n + 1):
	y = int(input())
	z += y
	if y > z / x: 
		print('>')
	elif y < z / x:
		print("<")
	else:
		print(0)