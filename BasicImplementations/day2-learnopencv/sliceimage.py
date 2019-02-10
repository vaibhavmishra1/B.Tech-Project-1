import cv2

image=cv2.imread("mom.jpg")
(h,w,c)=image.shape


roi=image[100:500 , 500:1000]
cv2.imshow("roi",roi)

cv2.waitKey(0)
