txt = input()
n = int(input())
lt = input()

if len(lt) > 1 or n > len(txt) or n < 1:
	print('ОШИБКА')
elif txt[n - 1] == lt:
	print('ДА')
elif txt[n - 1] != lt:
	print('НЕТ')