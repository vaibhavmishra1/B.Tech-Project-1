import cv2

image=cv2.imread("mom.jpg")
(h,w,c)=image.shape

print(h,w,c)
(b,g,r)=image[1000,1000]
print(b,g,r)
