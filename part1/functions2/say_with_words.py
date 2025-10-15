nums = {
	1: 'one',
	2: 'two',
	3: 'three',
	4: 'four',
	5: 'five',
	6: 'six',
	7: 'seven',
	8: 'eight',
	9: 'nine',
	10: 'ten',
	11: 'eleven',
	12: 'twelve',
	13: 'thirteen',
	14: 'fourteen',
	15: 'fifteen',
	16: 'sixteen',
	17: 'seventeen',
	18: 'eighteen',
	19: 'nineteen'
}

tens = {
	2: 'twenty',
	3: 'thirty',
	4: 'forty',
	5: 'fifty',
	6: 'sixty',
	7: 'seventy',
	8: 'eighty',
	9: 'ninety'
}


def number_in_english(number):
	en = ''
	if len(str(number)) == 3:
		if number // 100 > 0:
			en += f'{dict(list(nums.items())[:10])[number // 100]} hundred'
	ten = number % 100
	if ten > 0:
		if ten in nums.keys():
			if len(en) > 0:
				en += ' and '
			en += nums[ten]
		else:
			if len(en) > 0:
				en += ' and '
			if ten // 10 > 0:
				en += tens[ten // 10]
			if int(str(ten)[-1]) > 0:
				if ten // 10 > 0:
					en += ' '
				en += nums[int(str(ten)[-1])]
	if number == 0:
		en = 'zero'
	return en