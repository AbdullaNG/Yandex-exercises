nnum = int(input())
num = int(input())
count = 0
for x in range(nnum, num + 1):
	num4 = x // 1000
	num3 = x // 100 - num4 * 10
	num2 = (x// 10) % 10
	num1 = x % 10
	if (num4 == num3 and num4 != num2 and num4 != num1) or \
	(num4 != num3 and num4 == num2 and num4 != num1 ) or \
	(num4 != num3 and num4 != num2 and num4 == num1 ) or \
	(num4 == num3 and num4 == num2 and num4 != num1 ) or \
	(num4 != num3 and num4 == num2 and num4 == num1 ) or \
	(num4 == num3 and num4 == num2 and num4 == num1 ):
		continue
	elif (num3 == num2 and num3 != num1) or \
	(num3 != num2 and num3 == num1) or \
	(num3 == num2 and num3 == num1) or (num2 == num1):
		continue
	else:
		print(x)
	count += 1
print(f'There is/are {count} different number/s')