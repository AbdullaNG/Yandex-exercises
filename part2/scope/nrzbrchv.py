letters = 'уеыаоиУЕЫАОИ.,!?;:\'"()-'


def translate(txt):
	new = ''
	for i in txt:
		if i in letters:
			continue
		else:
			new += i
	new = [x.strip() for x in new.split()]
	global translated_text
	translated_text = ' '.join(new)