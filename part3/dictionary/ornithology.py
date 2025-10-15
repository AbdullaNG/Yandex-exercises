birds = {}
bird = 0

while True:
	bird = input().split(': ')
	if bird != ['']:
		bird[1] = int(bird[1])
		if bird[0] in birds.keys():
			birds[bird[0]] += bird[1]
		else:
			birds[bird[0]] = bird[1]
	else:
		print(birds)
		break