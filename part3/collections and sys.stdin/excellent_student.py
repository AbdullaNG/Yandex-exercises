classes = []
n = int(input())

for i in range(n):
	m = int(input())
	tp = []
	for j in range(m):
		s = input().split()
		student = s[1]
		tp.append(student)
	classes.append(any(map(lambda a: a == '5', tp)))

print('ДА' if all(classes) else 'НЕТ')