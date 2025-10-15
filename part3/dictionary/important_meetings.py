n = int(input())
meetings = []

for i in range(n):
	txt = input().split(', ')
	meetings.append(txt)

month = input()
choosen = [j[:2] for j in meetings if month in j]
choosen = [(int(x[1]), x[0]) for x in choosen]
choosen.sort()

for y in choosen:
	print(y[1])
