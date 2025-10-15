get = input()
ind = 0
lt = []

for i in get:
	ind += 1
	if i == '?':
		get = get[ind:]

get = get.split('&')

key = input()

for j in get:
	if j.split('=')[0] == key:
		print(j.split('=')[1])