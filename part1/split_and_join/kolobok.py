'''n = int(input())
nums = []
texts = []
same = 0
sames = []
last_txt = ''
count = 0
flag = True

for i in range(n):
	num = int(input())
	nums.append(num)

for j in range(n):
	txt = input()
	texts.append(txt)

for x in range(len(texts)):
	for y in range(len(texts[x])):
		for z in range(len(texts[x])):
			if texts[x][y] == texts[x][z]:
				same += 1
				s = texts[x][y]
		if nums[x] == same:
			if count == 0:
				sames.append(s)
			elif count > 1:
				flag = False
			count += 1
		same = 0
	count = 0

print(sames)

if flag:
	for k in sames:
		last_txt += k

	if len(last_txt) == n:
		print(last_txt)
	else:
		print('нечленораздельно')
else:
	print('нечленораздельно')'''




n = int(input())
nums = []
texts = []

for i in range(n):
	num = int(input())
	nums.append(num)

for j in range(n):
	txt = input()
	texts.append(txt)

c, d = '', ''
s, k, f, r, e = 0, -1, 0, 0, 0
flag = True

for i in texts:
	k += 1
	for j in range(len(i)):
		for h in range(len(i)):
			if i[j] == i[h]:
				s += 1
		if s == nums[k]:
			c += i[j]
		s = 0

for g in nums:
	f += g

if f != len(c):
	flag = False
	print('нечленораздельно', end='')

if flag:
	d = c[0]
for t in range(1, len(c)):
	if not flag:
		break
	if c[t] == c[t - 1] and r < nums[e]:
		r += 1
		continue
	r = 1
	e += 1
	d += c[t]

if f != len(c) and flag:
	print('нечленораздельно')
elif d == 'упс':
	print('нечленораздельно')
else:
	print(d)