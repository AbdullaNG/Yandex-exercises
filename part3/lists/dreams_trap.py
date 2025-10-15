txt = 0
dreams = []

while txt != '':
	txt = input()
	dreams.append(txt)

n1 = int(input()) - 1
n2 = int(input())
maxx = dreams[n1]

for i in dreams[n1:n2]:
	if len(i) > len(maxx):
		maxx = i
print(maxx)