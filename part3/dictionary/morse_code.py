txt = input().upper().split()
morse = {
			'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
			'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
			'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
			'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'
}
count = 0

for i in txt:
	for j in i:
		count += 1
		if count < len(i):
			print(morse[j], end=' ')
		else:
			print(morse[j])
	count = 0