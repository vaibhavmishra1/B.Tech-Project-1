import cv2
image=cv2.imread("mom.jpg")
cv2.imshow("image",image)
(h,w,c)=image.shape
k=cv2.GaussianBlur(image,(20,20),0)
cv2.imshow("ans",k)
cv2.waitKey(0)
