lt = []


def prompter(txt):
	global lt
	if lt == []:
		lt.append(txt)
		return txt
	else:
		flag = False
		for i in lt:
			if txt in i:
				flag = True
				return i
		if flag is False:
			lt.append(txt)
			return txt