import cv2
filePath = 'bunny1.jpg'
imgFlag = int(1)
img = cv2.imread(filePath,imgFlag)
cv2.imshow("Baby bunny",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

