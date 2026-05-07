
# matplotlib : 그래프와 이미지를 눈으로 볼 수 있게 해주는 시각화 라이브러리이다.

import numpy as np
import matplotlib.pyplot as plt

# x = [2023, 2024, 2025, 2026]
# y = [45, 34, 67, 51]

plt.rcParams["font.family"] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False   # 마이너스 표시

# x = np.arange(0,10)
# tm = np.random.randint(1,10, 10)
# y = tm*2
#
# plt.plot(x,y) # x축, y축 그래프 그리기 (기본 그래프는 세로 그래프)
#
# # plt.ylim(0,20) # y축 값 범위 지정
# plt.yticks(range(0,21,1)) # y축 범위 , 단위 지정
# plt.xticks(range(10))
#
# plt.title("랜덤 숫자") # plt.title : 제목 넣어주기
# plt.xlabel("count")
# plt.ylabel("number")
#
# plt.show()

x = ["자바", "스프링부트", "html", "데이터베이스", "파이썬", " css", "javascript", "진섭이는 게임을 못한다."]
y = [45,56,78,91,68,77,89,10]

# plt.figure( figsize=(30,20))
# figure 그래프가 그려지는 보드의 크기 지정
# (가로길이, 세로길이) , plot 이전에 설정

plt.plot(x,y)

plt.xticks(rotation=45) # 글씨끼리 겹칠경우 축을 회전시켜 겹치지 않게 한다.
plt.tight_layout() # 그래프 여백 자동 설정 (제일 많이 사용)

# 여백 설정하기 - top, left, right, bottom
# plt.subplots_adjust(bottom=0.3)

# dpi 저화질 - 72 , 고화질 - 300 , 중간 - 150
# transparent=True - 배경 투명하게(png)
plt.savefig("test.png", dpi=300, transparent=True) # 그래프 저장하기 (png,jpg,pdf 등)

plt.show()

