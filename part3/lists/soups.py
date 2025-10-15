soups = ['щи', 'борщ', 'щавелевый суп', 'овсяный суп', 'суп по-чабански']
n = int(input())

for i in range(n):
	print(soups[i % 5])