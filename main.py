import cv2
img = cv2.imread("test.png")
print(img.shape)
img = cv2.resize(img,(50,50))
print(img.shape)
cv2.imwrite("test1.png",img)
cv2.imshow("Show my pic",img)
cv2.waitKey(0)