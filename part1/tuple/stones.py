n = int(input())
s = 0
nums = []
flag = False
inc = 0
inc_nums = []

for i in range(n):
	num = int(input())
	s += num
	nums.append(num)

if s % 2 == 0:
	flag = True

for j in nums:
	if flag and j % 2 != 0:
		inc_nums.append(j)
		inc += j
	elif flag is False and j % 2 == 0:
		inc_nums.append(j)
		inc += j

for x in inc_nums:
	nums.remove(x)

print(inc, nums)