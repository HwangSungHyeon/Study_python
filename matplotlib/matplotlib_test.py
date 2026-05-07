'''
    125번 png와 json 파일을 사용하여 다음을 만들어 보시오

    이미지 안에서 차량의 크기가 가장 큰 차와 세번째로 큰 차를 바운딩 박스로 표시해주세요
    가장 큰 차의 바운딩 박스 테두리 색은 red
    세번째로 큰 차의 바운딩 박스 테두리 색은 yellow
'''

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image
import json
# colors = ("red", "yellow", "blue", "green", "lime", "magenta", "cyan", "purple")
pos = list()

with open('18396708_frame_125.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for ann in data['frames']['annotations']:
    code = ann['category']['code']
    if 'vehicle' != code:
        continue
    label = ann['label']
    pos.append((label['x'], label['y'], label['width'], label['height']))
pos = sorted(pos, key=lambda x: x[2] * x[3], reverse=True)[0:3:2]
# pos = pos[0:3:2]
print(pos)

img = plt.imread('18396708_frame_125.png') # 이미지 불러오기
plt.imshow(img) # 이미지 출력
ax = plt.gca()  # 이미지 좌표 가져오기
for i, (x,y,w,h) in enumerate(pos):
    if i == 0:
        color = 'red'
    else:
        color = 'yellow'
    box = patches.Rectangle(
        (x,y),
        w,
        h,
        fill=False,
        edgecolor=color,
        linewidth=2
    )
    ax.add_patch(box)
plt.show()
