a = "АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя"
num = int(input())
text = str(input())
total = 0
for x in range(len(text)):
	for y in range(len(a)):
		if text[x] == a[y]:
			y += num * 2
			if y > 64:
				y = y - 64
				print(a[y], end="")
			elif y <= 64:
				print(a[y], end="")
	if text[x] not in a:
		print(text[x], end="")