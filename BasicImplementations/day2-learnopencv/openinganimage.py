import cv2

image=cv2.imread("mom.jpg")
(h,w,c)=image.shape

print(h,w,c)
cv2.imshow("image",image)

cv2.waitKey(0)
