
import cv2

img = cv2.imread("opencv_study/images/cars.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur =  cv2.GaussianBlur(gray, (5,5), 0)

_, thresh = cv2.threshold(
    blur, 120, 255, cv2.THRESH_BINARY
)

contours, hier = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

result = img.copy()
count = 0

for contour in contours:
    area = cv2.contourArea(contour)
    if area > 200:
        count += 1

# cv2.drawContours( result, contours, -1, (0,0,255), 2)
print("차량 수 : ", count)

cv2.imshow("thr", thresh)
cv2.imshow("contour", result)
cv2.waitKey(0)
cv2.destroyAllWindows()