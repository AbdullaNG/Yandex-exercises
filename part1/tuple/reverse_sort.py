n = int(input())
nums = []

for i in range(n):
	num = int(input())
	nums.append(num)

for x in range(len(nums)):
	for y in range(len(nums)):
		if nums[x] > nums[y]:
			nums[x], nums[y] = nums[y], nums[x]

for z in nums:
	print(z)