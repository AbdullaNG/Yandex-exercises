text = input()
text_num = int(input())

if text_num > 0 and text_num <= len(text):
	print(text[text_num - 1])
else:
	print('ОШИБКА')