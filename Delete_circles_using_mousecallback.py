import cv2

def getxy(evt, x, y,flags, userdata):
    if evt == cv2.EVENT_LBUTTONDOWN:
        print("x:"+str(x)+ "y:"+str(y))
        value = im[y,x]
        print("B: "+str(value[0]) + "G: "+str(value[1]) + "R: "+str(value[2]))
        # cv2.circle(im,(x,y),10, (255,0,0), 2)
        circles.append([x,y])
        if evt == cv2.EVENT_RBUTTONDOWN:
            circles.clear()

im = cv2.imread("color_bars.png")
im1 = im.copy()
window_title = "color Bars"
circles = []
 
while True:
    print(circles)
    for circle in circles:
        cv2.circle(im1, (circle[0],circle[1]),10,  (255,0,0), 2)
        if len(circles)==0:
            im1 = im.copy()
    # cv2.circle(im,(x,y),10, (255,0,0), 2)
    cv2.imshow(window_title,im1)
    cv2.setMouseCallback(window_title,getxy,"Hello")
    ch = cv2.waitKey(10)
    if ch & 0xFF == ord('q'):#press q to quit the screen
        break

cv2.destroyAllWindows()