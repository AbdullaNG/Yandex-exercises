def line(s, t):
	if '+' in s:
		snum = float(s[:s.find('x')]) * float(t[:t.find(';')]) + float(s[s.find('+'):])
	else:
		tnum = s[s.find('x'):]
		snum = float(s[:s.find('x')]) * float(t[:t.find(';')]) + float(tnum[tnum.find('-'):])
	if float(t[t.find(';') + 1:]) == snum:
		print(True)
	else:
		print(False)