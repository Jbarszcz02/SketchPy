import cv2

zdjecie = cv2.imread("PHOTO URL")
cv2.imshow("Zdjecie", zdjecie)
cv2.waitKey(0)

szkic = cv2.cvtColor(zdjecie, cv2.COLOR_BGR2GRAY)
cv2.imshow("Ciemny", szkic)
cv2.waitKey(0)

obrZdj = 255 - szkic


blur = cv2.GaussianBlur(obrZdj, (21, 21), 0)

obrszkic = 255 - blur
oloszkic = cv2.divide(szkic, obrszkic, scale=256.0)
cv2.imshow("Szkic", oloszkic)
cv2.waitKey(0)