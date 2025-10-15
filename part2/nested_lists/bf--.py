cmd = input()
lt = [0 for i in range(30000)]
bot = 0
i = 0

while i < len(cmd):
	if cmd[i] == ">":
		if bot + 1 > 29999:
			bot = 0
		else:
			bot += 1
	elif cmd[i] == "<":
		if bot - 1 < 0:
			bot = 29999
		else:
			bot -= 1
	elif cmd[i] == ".":
		print(lt[bot])
	elif cmd[i] == "+":
		lt[bot] += 1
		if lt[bot] > 255:
			lt[bot] = 0
	elif cmd[i] == "-":
		lt[bot] -= 1
		if lt[bot] < 0:
			lt[bot] = 255
	elif cmd[i] == '[':
		if lt[bot] == 0:
			j = i + 1
			c = 1
			while(True):
				if cmd[j] == '[':
					c += 1
				if cmd[j] == ']':
					c -= 1
				if c == 0:
					i = j
					break
				j += 1
	elif cmd[i] == ']':
		c = - 1
		j = i - 1
		while(True):
			if cmd[j] == ']':
				c -= 1
			if cmd[j] == '[':
				c += 1
			if c == 0:
				i = j - 1
				break
			j -= 1
	i += 1