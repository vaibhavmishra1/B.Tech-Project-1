import cv2

image=cv2.imread("mom.jpg")
(h,w,c)=image.shape
center=(w//2,h//2)
k=cv2.getRotationMatrix2D(center,-45,1.0)
ans=cv2.warpAffine(image,k,(w,h))
cv2.imshow("ans",ans)
cv2.waitKey(0)
