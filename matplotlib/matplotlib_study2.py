
import numpy as np
import matplotlib.pyplot as plt

# img = np.array([
#     [0,50,100],
#     [150,200,255]
# ])
img = np.random.randint(0,256,(100,100))

# bright = np.clip(img+100, 0, 255) # clip - 설정한 범위를 넘지 않도록 해줌
# bright = 255 - img 반전효과

# 128 이상은 255변경 , 128미만은 0변경
copy_img = img.copy() # 원본 복사
copy_img[ copy_img >= 128] = 255
copy_img[ copy_img < 128] = 0

plt.figure(figsize=(8,4))

plt.subplot(1,2,1) # 1,2,1 -> 1행 2열에서 1열에 배치
plt.imshow(copy_img, cmap='gray')
plt.title("copy")
plt.axis('off')

plt.subplot(1,2,2) 
plt.imshow(copy_img, cmap='gray') # cmap='gray' - 흑백으로 바꾸기
plt.title("original")
plt.axis('off') # 축 삭제

plt.show()