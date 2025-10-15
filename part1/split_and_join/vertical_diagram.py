
nums = input().split()
nums = [int(i) for i in nums]
maxx = int(nums[0])

for x in nums:
	if x > maxx:
		maxx = x

print('*' * (len(nums) + 2))

for i in range(maxx + 1):
	print(end='*')
	for z in nums:
		if int(z) >= maxx - i + 1:
			print(end='*')
		else:
			print(end=' ')
	print('*')