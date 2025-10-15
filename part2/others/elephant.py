parts = ''
trunk_num = 0
tail_num = 0
leg_num = 0
ear_num = 0
eye_num = 0
mouth_num = 0
elephant = 0

while parts != 'ОБЕД':
	part_num = int(input())
	parts = input()

	if part_num >= 1 and parts == 'хобот':
		trunk_num += part_num
	elif part_num >= 1 and parts == 'хвост':
		tail_num += part_num
	elif part_num >= 1 and parts == 'нога':
		leg_num += part_num
	elif part_num >= 1 and parts == 'ухо':
		ear_num += part_num
	elif part_num >= 1 and parts == 'глаз':
		eye_num += part_num
	elif part_num >= 1 and parts == 'рот':
		mouth_num += part_num

	if trunk_num > 0 and tail_num > 0 and leg_num >= 4 and ear_num >= 2 and eye_num >= 2 and mouth_num >= 1:
		print('Есть слон!')

		while trunk_num > 0 and tail_num > 0 and leg_num >= 4 and ear_num >= 2 and eye_num >= 2 and mouth_num >= 1:
			elephant += 1
			trunk_num -= 1
			tail_num -= 1
			leg_num -= 4
			ear_num -= 2
			eye_num -= 2
			mouth_num -= 1
		print(elephant)
		break
if elephant == 0:
	print('Какие-то слоны нецелые. Пошли обедать.')