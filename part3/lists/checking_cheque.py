nsum = input()
n = int(nsum[:4])
sum = int(nsum[4:])
miss = []
true_sum = 0 

for i in range(n):
	nsum = input()
	price = int(nsum[:7])
	amount = int(nsum[8:12])
	tot = int(nsum[13:])

	if price * amount != tot:
		miss.append(i + 1)

	true_sum += price * amount

print(sum - true_sum)

for x in miss:
	print(x, end=' ')