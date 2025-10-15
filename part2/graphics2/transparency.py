from PIL import Image


def transparency(filename1, filename2):
	img1 = Image.open(filename1)
	img2 = Image.open(filename2)
	px1 = img1.load()
	px2 = img2.load()
	width, height = img1.size
	for x in range(width):
		for y in range(height):
			r1, g1, b1 = px1[x, y]
			r2, g2, b2 = px2[x, y]
			px3 = (int(0.5 * r1 + 0.5 * r2), int(0.5 * g1 + 0.5 * g2), int(0.5 * b1 + 0.5 * b2))
			px1[x, y] = px3
	img1.save("res.jpg")


transparency("image1.jpeg", "image2.jpeg")