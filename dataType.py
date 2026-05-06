# 리스트, 튜플
# 리스트 - 여러 데이터를 저장 관리하기 위한 파이썬 자료구조이다.
# 튜플도 리스트와 같은데 차이점은 리스트는 수정이 가능하지만 튜플은 수정이 불가능하다.

# 리스트 - 순서 유지, 인덱스를 통해 접근, 추가, 수정, 삭제 가능
# 다른 자료형도 저장 가능
number = [10, 20, 30, 40, 50]
emtpy = []
name = list()

print( number[0] )
print( number[-2] )

# 리스트 자르기
num = number[2:4] # 2번 인덱스부터 4번 인덱스 전까지 자르기
print(num)
num2 = number[:3] # 처음부터 3번 인덱스 전까지 자르기
print(num2)
num3 = number[2:] # 2번 인덱스부터 끝까지 자르기
print(num3)
num4 = number[:] # 전체 자르기
print(num4)
num5 = number[::-1] # 역순으로 뒤집기
print(num5)

# 리스트 수정
number[2] = 100
print(number)

# 리스트 추가
number.append(60) # 리스트 맨 뒤에 60 추가
print(number)

number.insert(2, 500) # 2번 인덱스에 500 추가
print(number)

# 리스트 값 삭제 ( 존재하지 않는 데이터와 인덱스를 입력하면 에러 )
number.remove(100) # 리스트에서 삭제할 데이터 입력
print(number)

number.pop(2) # 리스트에서 삭제할 인덱스 입력
print(number)

del number[0] # 인덱스로 삭제
print(number)

# 리스트 크기 (길이)
print( len(number) )

for num in number: # 리스트에 저장된 데이터 하나씩 꺼내서 num에 저장
    print(num)

for i , num in enumerate(number): # 리스트에 저장된 데이터 하나씩 꺼내서 num에 저장, 인덱스는 i에 저장
    print(i, num)

# 리스트 검색
print( 40 in number ) # 값의 존재여부 True, False
print( number.index(50) ) # 인덱스 찾기 (존재한다면 인덱스 값, 존재하지 않으면 에러)
# index를 통해 인덱스를 찾기 전에 in으로 존재여부 확인 먼저하기

# 리스트 정렬
number.sort() # 기본 정렬 : 오름차순 정렬
print(number)
number.sort(reverse=True) # 내림차순 정렬
print(number)

# 리스트는 일반적으로 많이 사용되는 자료구조이다.
#  자바에서 List (ArrayList)를 많이 사용 된다면 파이썬은 리스트이다.
#  여러데이터를 저장할 수 있고, 수정, 추가 기능하고 반복문 사용 쉽고
#  정렬, 검색도 되고 그래서 사용하기 좋은 자료구조이다.


# 리스트 문제 풀기!
#  문제1. - 5명의 이름이 저장되어 있는 리스트 만들기
#         5명의 이름 출력하는 반복문 만들기
names = ["홍길동", "김철수", "이영희", "박민수", "최지우"]
for n in names:
    print(n)

# 문제2. - 정도전 이름을 추가하고 출력하세요
names.append("정도전")
print(names)

# 문제 3. - 리스트에 김유신이 있는지 확인하는 코드 작성하기
if "김유신" in names:
    print("등록된 이름이다.")
else:
    print("등록되지 않은 이름이다.")

# 문제 4. - 이름 리스트에 내림차순으로 정렬하여 출력하세요
names.sort(reverse=True)
print(names)

# 문제 5. - 과일의 이름이 두글자인 과일만 출력하세요
# 힌트 : len
fruits = ["사과", "바나나", "파인애플", "딸기", "오렌지", "포도" ,"배"]
for f in fruits:
    if len(f) == 2:
        print(f)
# fruit = [i for i in fruits if len(i) == 2]
# print(fruit) 이렇게 하면 리스트로 나옴.

fruits.sort(key=len) # key는 정렬 기준이 되는 함수 len은 문자열의 길이
print(fruits)

# 문제 6. - 과일 검색 프로그램 만들기
#   과일이름 키보드를 통해 입력받는다.
#   입력한 과일이 리스트에 있다면 판매중, 없다면 품절이라고 출력

# user = input("과일 이름을 입력하세요 : ").strip()
# if user in fruits:
#     print("판매중")
# else:
#     print("품절")

# isexists = False
# for f in fruits:
#     if user == f:
#         isexists = True
# if isexists:
#     print("판매중")
# else:
#     print("품절")

# 문제 7. - 구매하고자 하는 과일을 입력 하면 총 지불금액 얼마인지 출력
#   단, 과일은 1개를 구매할 수 도 있고 여러개 구매할 수 도 있어야 한다.
# fruits.sort() # 딸기, 바나나, 배, 사과, 오렌지, 파인애플, 포도 순
# price = [5000, 8000, 12000, 9500, 15500, 20400, 9000]

# user = input("구매하고자 하는 과일 입력: ").split()

# # total = sum(price[fruits.index(f)] for f in user)
# # print("총 지불금액 : ", total)
# total = 0
# for f in user:
#     if f in fruits:
#         idx = fruits.index(f)
#         total += price[idx]
# print("총 지불금액 : ", total)

# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# 튜플 - 리스트처럼 여러 데이터를 저장할 수 있는 자료형이다.
#   저장한 데이터를 수정할 수 없다.
#   데이터를 보호하기 위한 목적
#   속도와 메모리 효율성
#   딕셔너리의 키로 튜플이 사용됨 - 왜냐 key는 수정되면 안되니까
#   여러개의 값을 반환(return) 시킬 때

# 튜플 만들기
number = (10,20,30,40) # 작은괄호 - 튜플, 대괄호 - 리스트
print(number)
print( type( (1,2,3,4) ))
print( type( (10,) )) # 값이 하나만 들어가면 튜플로 들어가지 않고 값을 하나만 넣고 싶으면 ,를 붙여야 한다.

print( number[1] ) # 인덱스 0 부터 시작

# 튜플 슬라이싱( 자르기 ) 리스트와 동일
print( number[1:3] )

# 튜플 검색
print( 10 in number )
print( number.index(20) )

# 리스트와 다른점
# 수정 불가, 추가 불가, 삭제 불가
# number.append(200) 오류
# number.remove(20) 오류
# number.pop(20) 오류
# del number[2]

print( number.count(20) ) # 특정값 갯수 구하기

data = 10,20,30,40,50  # 패킹 - 여러값을 하나로 묶기
print( type(data) )

a,b,c,d,e = data  # 언패킹 - 묶여있는 값을 여러개로 나누기
print( a,b,c,d,e )

# 값을 바꿔줄때 파이썬에선 패킹, 언패킹으로 쉽게 바꿀 수 있다.
red = 20
blue = 10

red, blue = blue, red
print(red, blue)

# 함수 반환 여러개
def get():
    return 10,20,30,40


# 리스트 <--> 튜플
info = ("다음주","금요일","빨간날","그래서","우리는","5월6일에","봐요")
# info[0] = "이번주"
info_list = list(info) # 튜플 -> 리스트로 변환 시켜주는 방법
info_list[0]="이번주"

info = tuple(info_list) # 리스트 -> 튜플로 변환 시켜주는 방법
print(info)

