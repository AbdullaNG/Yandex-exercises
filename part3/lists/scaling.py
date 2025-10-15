h = int(input())
w = int(input())
image = []

for i in range(h):
	img = input()
	image.append(img)
for j in image[::2]:
	print(j[::2])