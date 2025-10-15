n = int(input())
sym = 0
title = []
all_titles = []

txt = input()
while sym < n:
	if txt != '*':
		title.extend(txt.split())
	txt = input()
	if txt == '*':
		x = '-'.join(title)
		all_titles.append(x)
		title = []
		sym += 1

print(', '.join(all_titles[::-1]))