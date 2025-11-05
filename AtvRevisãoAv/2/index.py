import cv2
img = cv2.imread("bio.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Minha janela", img)
cv2.imshow("Em cinza", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()