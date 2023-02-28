import cv2

image = cv2.imread('C:/Users/e1356/python/open_cv/apple_soda.jpg')
resize_img = cv2.resize(image, (400, 800))


img_gray = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)


cv2.imshow('image_apple', img_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
