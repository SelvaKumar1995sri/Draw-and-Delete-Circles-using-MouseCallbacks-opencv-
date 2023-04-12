from rembg import remove
from PIL import Image
import easygui as eg
import cv2

img = cv2.imread("Stencil_2.jpg")

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])

im1_s = cv2.resize(img, dsize=(0, 0), fx=0.1, fy=0.1)
im_tile = concat_tile([[im1_s, im1_s, im1_s, im1_s],
                       [im1_s, im1_s, im1_s, im1_s],
                       [im1_s, im1_s, im1_s, im1_s]])
cv2.imwrite('opencv_concat_tile.jpg', im_tile)

# b = cv2.imshow("texture", im_tile)
# print(b)
# # cv2.waitKey(0)


input_path = eg.fileopenbox(title='Select image file')
output_path = 'masked.png'
input = Image.open(input_path)
output = remove(input, alpha_matting=True)
output.save(output_path)

background_image = 'opencv_concat_tile.jpg'
background_image = Image.open(background_image)

background_image = background_image.resize((input.width,input.height))

foreground_img = Image.open(output_path)
background_image.paste(foreground_img, (0,0), foreground_img)
background_image.save('result.jpg')

