from PIL import Image


def mirror():
	img = Image.open('image.jpg')
	img = img.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)
	img = img.transpose(method=Image.Transpose.ROTATE_270)
	img.save('res.jpg')


mirror()