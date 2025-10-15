'''n1 = int(input())
n2 = int(input())
low = False

while n2 != 0:
	if low == False:
		if n1 < n2:
			low = True
			num1 = n2
	if low == True:
		if n1 > n2:
			num2 = n2
	n1 = n2
	n2 = int(input())

print(num1, num2, num2 - num1)'''


b = 0
st = 0
end = 0

while  True:
	a = int(input())
	if a == 0:
		break
	if b != 0:
		if st == 0:
			if a > b:
				st = a
		elif end == 0:
			if a < b:
				end = a
	b = a

print(st, end, end - st)