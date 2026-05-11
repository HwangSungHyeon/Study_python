
# open source Computer vision lib
# 컴퓨터 비전 - 비전AI

# 이미지 - 사람이다, 파란색이다, 하늘색이다, 고양이다, 멍멍이다.
# 컴퓨터는 픽셀 숫자들의 모음으로 보고 있다.

# opencv로 이미지나 영상을 불러오기
# yolo에게 전달하여 객체 탐지
# 탐지 결과를 토대로 이미지나 영상에 opencv로 표시하기
# opencv - BGR (RGB랑 순서가 반대)
# arr = np.array([ [0,50,100] , [150,200,255] ])
# 영상 - opencv 열기 -> 프레임 한장 열기 -> 이미지 처리 -> 다음프레임 읽기 -> 이미지 처리

# 앞으로 할것
#   이미지 필터, 객체 외곽선 찾기
#   움직임 감지, 영상 저장, 객체 탐지 결과 시각화

#   이미지는 numpy 배열로 봐야한다.
#   영상은 이미지 여러장이다.
#   프레임 하나는 이미지 한장이다. fps( frame per second )

import cv2

img = cv2.imread("opencv_study/images/cat.png")

# cv2.imshow("이미지창 제목", 표시할 이미지)


print( type(img) ) # numpy 배열 타입
print( img.shape) # 세로, 가로, 색상값 - 3은 rgb
# 색상정보 - 1은 흑백, 4는 투명도 포함(BGRA, RGBA)
# (183,275,1) - 픽셀하나에 숫자 1개
# (183,275,1) - 픽셀하나에 숫자 3개 (B,G,R,A)
#             A는 알파( 투명도 - 0 (투명) ~ 255 (불투명) )

# print(img[100][100])
# copy_img = img.copy() # 원본데이터를 변경하지말고 복사본으로
# copy_img[100:200, 100:200] = [0,0,255]
# cv2.imshow("image",copy_img)
# # 이미지 저장 .imwrite("저장할 파일명", 저장객체)
# cv2.imwrite("opencv_study/images/copy_cat.png", copy_img)
# cv2.waitKey(0)

# # (134,229,127) - RGB 색상값
# # cat 이미지 정중앙에 위 RGB 색상으로 가로세로 50픽셀 채우기

# copy_img1 = img.copy()

# h,w = img.shape[:2]

# centerY = h // 2
# centerX = w // 2

# # copy_img1[centerX-25:centerX+25, centerY-25:centerY+25] = [127,229,134]
# cv2.rectangle(
#     copy_img1,
#     (centerX-25 , centerY-25),
#     (centerX+25 , centerY+25),
#     (127,229,134),
#     -1
# )

# cv2.imshow("image",copy_img1)
# cv2.imwrite("opencv_study/images/copy_cat.png", copy_img1)
# cv2.waitKey(0)


# 고양이 얼굴 부분만 자르기
copy_img = img.copy()

cut = copy_img[20:120, 130:230] # 2차원 배열에서 범위를 슬라이싱할때 [y축:x축, y축:x축] 이다.
cv2.imwrite('opencv_study/images/cut_cat.png', cut)
cv2.imshow("cut",cut)
cv2.waitKey(0)