from rembg import remove
from PIL import Image
import easygui as eg



input_path = eg.fileopenbox(title='Select image file')
output_path = 'masked/masked.png'
input = Image.open(input_path)
output = remove(input, alpha_matting=True)
output.save(output_path)

background_image = "texture/Stencil_2.jpg"
background_image = Image.open(background_image)

background_image = background_image.resize((input.width,input.height))

foreground_img = Image.open(output_path)
background_image.paste(foreground_img, (0,0), foreground_img)
background_image.save('masked/result.jpg')