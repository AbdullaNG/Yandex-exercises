from PIL import Image


R, G, B = 0, 0, 0
img = Image.open('image.jpg')
px = img.load()
x, y = img.size

for i in range(x):
	for j in range(y):
		r, g, b = px[i, j]
		R += r
		G += g
		B += b

print(R // (x * y), G // (x * y), B // (x * y))