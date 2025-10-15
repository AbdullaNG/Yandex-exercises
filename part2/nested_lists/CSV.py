table = []
nums = []
r = int(input())

for i in range(r):
	td = input().split(',')
	table.append(td)

n = int(input())

for j in range(n):
	num = [int(x) for x in input().split(',')]
	nums.append(num)

for z in range(n):
	print(table[nums[z][0]][nums[z][1]])