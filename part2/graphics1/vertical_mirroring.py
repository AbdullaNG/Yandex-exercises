from PIL import Image


def mirror():
	img = Image.open('image.jpg')
	img2 = img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
	img2.save('res.jpg')