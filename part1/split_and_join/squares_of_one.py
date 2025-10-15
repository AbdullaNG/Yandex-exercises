n = int(input())
y = [x * x for i in range(1, 1000) if (x := int('1' * i)) < n]
for i in range(len(y) - 1):
	print(y[i], end=', ')
print(y[-1])