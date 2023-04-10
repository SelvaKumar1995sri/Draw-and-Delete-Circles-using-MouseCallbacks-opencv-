import cv2
import matplotlib.pyplot as plt


img = cv2.imread("colourWall.jpg")
cImg = img.copy()
img = cv2.blur(img, (5, 5))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

scale = 1
delta = 0
ddepth = cv2.CV_16S

grad_x = cv2.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)
grad_y = cv2.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv2.BORDER_DEFAULT)

abs_grad_x = cv2.convertScaleAbs(grad_x)
abs_grad_y = cv2.convertScaleAbs(grad_y)

grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

ret, thresh = cv2.threshold(grad, 10, 255, cv2.THRESH_BINARY_INV)


image_copy = img.copy()
c, h = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(image_copy, c, -1, (0,255,0), 2)
# plt.imshow(image_copy[:,:,::-1]);plt.title("contours");plt.axis("off")
# plt.show()

areas = [cv2.contourArea(c1) for c1 in c]
maxAreaIndex = areas.index(max(areas))

cv2.drawContours(cImg, c, maxAreaIndex, (255, 0, 0), -1)

plt.imshow(cImg)
plt.show()