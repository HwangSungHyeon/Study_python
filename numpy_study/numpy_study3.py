
import numpy as np

# 배열에서 원하는 위치 데이터 가져오기

arr = np.random.randint(0,50, 12)
print(arr)

# 슬라이싱
print( arr[3:8] )
print( arr[:4] ) # :4 -> 0번 인덱스부터 3번까지
                 # 2: -> 2번 인덱스부터 끝까지
print( arr[::2] ) # ::2 -> 2칸씩
print( arr[::-1] ) # ::-1 -> 역방향으로 출력

arr2 = np.random.randint(0,50,(3,4) )
print(arr2)
print( arr2[1] )
print( arr2[:, 2] )
print( arr2[0:1, 1:3])

# fancy indexing : 원하는 위치만 고르기
print( arr[[0,4,7]])  # [ [ 인덱스, 인덱스 ] ] 원하는 인덱스 번호 넣기

print( arr2[[0,2]]) # 2차원 배열에서는 행을 선택
print( arr2[[0,2], [1,3] ] )  # 인덱스 0행의 1열 과 인덱스 2행의 3열

# boolean indexing
print( arr > 30 ) # True , false 로 나옴
print( arr[ arr>30] ) # 30보다 큰 값이 바로 나옴
print( arr[arr % 2 == 1] ) # 홀수인 값만 뽑아서 나옴

print( arr2[ arr2 > 15] )

# 학생 5명의 6과목 성적을 배열로 저장하세요 (성적은 50~100 사이 임의값)
# 학생 5명 성적이 저장된 배열에서 성적이 80점 이상만 출력하시오

arr3 = np.random.randint(50,100, (5,6))
print(arr3)
print( arr3[ arr3>=80] )

pos = np.argwhere( arr3 >= 80 ) # 인덱스 좌표가 뜬다.
print( pos )