x = ''

while x != 0:
	x = int(input())
	if x % 3 != 0 and x % 7 != 0:
		print(x)
	elif x % 3 == 0 and x % 7 != 0:
		print('несчастливое')
	elif x % 7 == 0 and x % 3 != 0:
		print('опасное')
	elif x % 7 == 0 and x % 3 == 0 and x != 0:
		print('Караул!')
		break