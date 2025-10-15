summ = 0
count = 0


while True:
	if summ < 10:
		num = int(input())
		summ += num
		count += 1
	else:
		break

print(count)