nums = [int(i) for i in input().split()]
bin_num = ''
bin_nums = []
chs = []
d = {}

for x in nums:
	while x > 0:
		if x == 0:
			bin_num += '1'
		else:
			bin_num += str(x % 2)
		x //= 2
	bin_nums.append(bin_num[::-1])
	bin_num = ''

for y in bin_nums:
	d['digits'] = len(y)
	d['units'] = y.count('1')
	d['zeros'] = y.count('0')
	chs.append(d)
	d = {}

print(chs)