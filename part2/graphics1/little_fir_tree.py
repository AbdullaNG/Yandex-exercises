from PIL import Image, ImageDraw


s = int(input())
img = Image.new('RGB', (s * 24, s * 40), (255, 255, 255))
pen = ImageDraw.Draw(img)

pen.polygon((12 * s, 3 * s, 18 * s, 11 * s, 6 * s, 11 * s), ('#00b050'))
pen.polygon((12 * s, 8 * s, 20 * s, 20 * s, 4 * s, 20 * s), ('#00b050'))
pen.polygon((12 * s, 16 * s, 22 * s, 32 * s, 2 * s, 32 * s), ('#00b050'))
pen.rectangle((10.5 * s, 32 * s, 13.5 * s, 36 * s), ('#7f6000'), width=10)

img.save('fir_tree.png')