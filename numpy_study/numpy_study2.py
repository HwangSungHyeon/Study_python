
import numpy as np

# 배열 자동 생성
a = [ num for num in range(1,11) ]
print(a)

# arange(시작, 끝, 증가값)
arr = np.arange(1,11,2) # 배열 자동생성 : arange(숫자)
print(arr)

arr = np.arange(1,16) # 1부터 15까지
arr2 = arr.reshape(3, 5) # 1차원 배열을 -> 3행 5열의 2차원배열로 변환
# 차원 변경시 데이터 갯수가 일치해야한다. 4행 5열로 하면 오류
print(arr2)

arr3 = arr.reshape(5, -1) # -1 은 numpy가 알아서 계산해준다.
print(arr3)

dim1 = np.arange(24)
dim3 = dim1.reshape(3, -1, 2) # 4행 2열이 3개 만들어진다.
print(dim3)
dim_origin = dim3.reshape(dim3.size) # size 를 이용해서 1차원배열로 변환
print(dim_origin)

# 0으로 채워진 배열 생성
zero_arr = np.zeros((3,3), dtype=int) # 정수형으로 만드려면 dytpe=int
print("0으로 채우기", zero_arr)

# 1로 채워진 배열 생성
one_arr = np.ones((10), dtype=int)
print(one_arr)


# 문제2.
# 11부터 22까지의 숫자 12개를 배열에 저장하기
# 위에서 만든 배열을 2차원 배열 3행으로 만들기
#  2차원 배열의 2행 전체의 총합 구하기
#  2차원 배열 전체의 평균 구하기

arr11 = np.arange(11,23)
print(arr11)
arr22 = arr11.reshape(3,-1)
print(arr22)
print( arr22[1].sum())
print( arr22.mean())