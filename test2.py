# 문제 1. 간단한 함수만들기
#   사각형의 너비와 높이를 받아서 넓이를 출력하는 함수를 만들어 호추해보세요
#   함수에서 넓이 구하는 게산식이 있어야 하고 출력도 있어야 한다.

# width = int(input("너비 : "))
# height = int(input("높이 : "))
# def square(width, height):
#     extent = width * height
#     print("넓이 : ",extent)
# square(width,height)


# 문제 2. 아래 코드를 보고 함수를 만드세요.
#   로그인 체크 함수 만들기

# id = input("아이디를 입력하세요 : ")
# pw = input("비밀번호를 입력하세요 : ")
# def id_check(id):
#     if id == "admin" and pw == "1234": # 여기 부분을 함수로 처리될 수 있게
#         print("로그인 성공 하였습니다.")
#     else:
#         print("아이디 또는 비밀번호를 잘못 입력 하였습니다.")
# id_check(id)

# 문제3. 상품의 재고를 확인하여 재고 충분, 재고 부족, 품절 이라고 출력할 수 있는 함수만들기
#   재고 부족 기준은 현재 재고량이 8이하인 경우

# item_stock = 12
# def acount(item_stock):
#     if item_stock > 8:
#         return("재고 충분")
#     elif item_stock > 0:
#         return("재고 부족")
#     else:
#         return("품절")
# print(acount(item_stock))

# 문제4. 회원가입을 한다. 아이디 중복체크 함수를 만드세요.

# id_list = ["kim","lee","sky","gold","war123","qwer12","eeee14"]

# id_list는 현재 가입된 회원들의 아이디만 저장된 리스트이다.
# 아이디 중복체크 함수를 통해 사용가능, 불가능을 출력하세요

# id = input("아이디를 입력하세요 : ")
# def id_check(id):
#     if id in id_list:
#         return("사용 불가능")
#     else:
#         return("사용 가능")
# print(id_check(id))

# 문제. 숫자 하나를 받아서 짝수/ 홀수를 반환하는 함수 만들기
#   print(함수(숫자)) 형태로 실행

def info(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"
print(info(4))

# 문제. 이름과 나이를 받아서 아래처럼 출력하는 함수 만들기

def info(name, age):
    print(name,"님은",age,"살입니다.")
info("홍길동",20)

# 문제. 숫자 3개를 받아서 가장 큰 수를 반환하는 함수 만들기

def max_num(a,b,c):
    return max(a,b,c)
print(max_num(3,7,5))

# 문제. 리스트를 받아서 총합을 반환하는 함수 만들기

num_list = [10,20,30]

def total(num):
    return sum(num)
print(total(num_list))

# 문제. 리스트를 받아서 짝수만 출력하는 함수 만들기

list = [1,2,3,4,5]

def even_only(num1):
    for n in num1:
        if n % 2 == 0:
            print(n, end = " ")
even_only(list)

# 문제. 점수를 받아서 등급을 반환하는 함수 만들기
# 90 이상 -> A, 80이상 -> B, 70이상 -> C, 그 외 -> D
print("")

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"
print(grade(60))