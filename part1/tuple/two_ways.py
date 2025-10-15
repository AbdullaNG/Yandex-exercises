n = int(input())
b1 = [int(input()) for i in range(n)]
b2 = b1[:]
t = int(input())

for i in range(t):
	b = int(input())
	if b == 1:
		b1[int(input())] += int(input())
	elif b == 2:
		b2[int(input())] += int(input())

for x in b1:
	print(x, end=' ')
print()

for y in b2:
	print(y, end=' ')

print()

d = 0

for i in range(len(b1)):
	if b1[i] == b2[i]:
		d = d + 1
		
print(d)