from PIL import Image, ImageDraw


img = Image.new('RGB', (512, 200), (0, 0, 0))
pen = ImageDraw.Draw(img)


def gradient(color):
	for i in range(512):
		if color.upper() == 'R':
			pen.line((i, 0, i, 200), (i // 2, 0, 0), 1)
		elif color.upper() == 'G':
			pen.line((i, 0, i, 200), (0, i // 2, 0), 1)
		elif color.upper() == 'B':
			pen.line((i, 0, i, 200), (0, 0, i // 2), 1)
	
	img.save('res.png')


gradient('r')