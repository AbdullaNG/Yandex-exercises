from PIL import Image
 
 
def twist_image(input_file_name, output_file_name):
    image = Image.open(input_file_name)
    width, height = image.size
    left_image = image.crop((0, 0, width // 2, height))
    right_image = image.crop((width // 2, 0, width, height))
    new_image = Image.new('RGB', (width, height))
    new_image.paste(right_image, (0, 0))
    new_image.paste(left_image, (width // 2, 0))

    new_image.save(output_file_name)


twist_image('cube.jpg', 'new_cube.jpg')