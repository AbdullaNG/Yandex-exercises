sentence = input()
count = 0

for i in range(len(sentence)):
	count += 1
	if len(sentence) == count:
		print(ord(sentence[i]))
	else:
		print(ord(sentence[i]), end=', ')