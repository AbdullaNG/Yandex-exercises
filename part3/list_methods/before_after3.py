nums = input().split()
nums = [int(i) ** 2 for i in nums]
betwn = input().split()
print(sum(nums[int(betwn[0]):int(betwn[1]) + 1]))