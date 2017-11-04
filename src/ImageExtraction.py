import cv2

img=cv2.imread("lady.jpeg")
out=img[246:320,132:173]
cv2.imwrite("Cropped.jpeg",out)
cv2.waitKey(0)
print("hi")