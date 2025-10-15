import math


x = float(input())
if int(str(int(x * 1000))[-1]) >= 5:
	print(math.ceil(x * 100) / 100)
elif len(str(x)[str(x).find('.') + 1:]) < 3:
	print(x)
else:
	print(math.floor(x * 100) / 100)