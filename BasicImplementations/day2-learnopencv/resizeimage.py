import cv2

image=cv2.imread("mom.jpg")
(h,w,c)=image.shape


k=cv2.resize(image,(300,300))
cv2.imshow("resized",k)

cv2.waitKey(0)
