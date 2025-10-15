nums = [int(i) for i in input().split()]
txt = input().lower().split()
count = 0

for j in nums:
	count += 1
	if count == 1:
		print(txt[j - 1].capitalize(), end=' ')
	else:
		print(txt[j - 1], end=' ')