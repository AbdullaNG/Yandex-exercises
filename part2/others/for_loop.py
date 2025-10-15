'''z = int(input())
a = 1
odd = 0
even = 0
for x in range(1, z + 1):
	if a % 2 != 0:
		y1 = int(input())
		odd += y1
	elif a % 2 == 0:
		y2 = int(input())
		g = 0 - y2
		even += g
	a += 1
print(odd + even)'''

# z = int(input())
# odd = 0
# even = 0
# for x in range (1, z + 1):
# 	y = int(input())
# 	for i in range(1, z + 1, 2):   for sum only!
# 		odd += y
# 	for j in range(2, z, 2):
# 		g = 0 - y
# 		even += g
# print(odd + even)

z = 0
g = 0
x = int(input())
for i in range(x):
    z += 1
    a = int(input())
    while z % 2 == 0:
        g = g - a
        break
    while z % 2 != 0:
        g = g + a
        break
print(g)