lt = []


def print_only_new(message):
	global lt
	if message not in lt:
		lt.append(message)
		print(message)