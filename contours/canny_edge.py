import cv2
import numpy as np
"""
img = cv2.imread("contours/IMG_20230412_091134.jpg")
img = cv2.resize(img, (600,600))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(img_gray, 500,200)

cv2.imshow("original",img)
cv2.imshow("gray image",img_gray)
cv2.imshow("canny image",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""
img = cv2.imread("contours/IMG_0156.jpg")
img = cv2.resize(img, (500,500))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass
cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold","Canny",0,255,nothing)

while True:
    a = cv2.getTrackbarPos("Threshold","Canny")
    print(a)
    res = cv2.Canny(img_gray,a , 255)
    cv2.imshow("Canny",res)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        break

# cv2.destroyAllWindows()
