
import numpy as np
arr = np.array([10,20,30,40,50]) # numpy 배열 생성 - np.array()
print(arr)
print( type(arr))
print( arr[0])
print( arr[-2])
arr[0] = 100
print( arr[0])
print( [1,2,3] + [4,5,6] ) # 그냥 배열을 합치는 것
print( np.array([1,2,3]) + np.array([4,5,6]) )

print( arr + 10 )

print( len(arr) )
print( arr.shape ) # (5,) : 데이터 5개가 들어있는 1차원 배열 이라는 뜻
print( arr.dtype )
# int32, int64  -  정수타입
# float32, float64  -  실수
# uint8  -  이미지
# bool  -  논리 타입

score = np.array( [88, 94, 53, 67, 72])
print( "점수 : ", score )

print("평균 : ", score.mean())  # 평균은 .mean()

print( "총합 : ", score.sum())  # 총합은 .sum()

print( "최대값 : ", score.max())
print( "최솟값 : ", score.min())

# 이미지 또는 영상 shape 결과 - (720, 1280, 3) : 3차원 배열

'''
numpy는 파이썬에서 숫자 계산을 빠르게 하기 위한 라이브러리이다.
1+2+3
[1,2,3] + [4,5,6]

'''