from PIL import Image, ImageDraw

image = Image.open("picture.jpg")
draw = ImageDraw.Draw(image)

draw.rectangle((200,400,700,600), mask=(255,0,0), outline='yellow', width=5)
image.show()

# masking

# mask = Image.open(".png")
# image_masked = Image.alpha_composite(panda.convert('RGBA'),mask)

# image_masked.show()