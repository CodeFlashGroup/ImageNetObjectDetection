import cv2
#img=cv2.imread("C://Users//MAITRI SHAH//PycharmProjects//MLProject//kaggleImageNet//img//lady.jpeg")
img=cv2.imread("../img/lady.jpeg")
out=img[246:320,132:173]
cv2.imwrite("Cropped.jpeg",out)
cv2.waitKey(0)
print("hi")