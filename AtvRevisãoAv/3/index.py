import cv2
img = cv2.imread("raizen.png")
# Reduz para metade
small = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# Aumenta para o dobro
large = cv2.resize(img, (0,0), fx=2, fy=2)
cv2.imshow("Imagem Original", img)
cv2.imshow("Pequena", small)
cv2.imshow("Grande", large)
cv2.waitKey(0)
cv2.destroyAllWindows()