word = input()
word1 = ''

for i in word:
	if i == ' ':
		continue
	else:
		word1 += i

if word1 == word1[::-1]:
	print(True)
else:
	print(False)