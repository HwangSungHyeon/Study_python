
# 딕셔너리
# 딕셔너리는 데이터를 키와 value로 저장하는 자료형 이다.

info = { "name" : "이순신" } # name이 key, 이순신이 value
print( info["name"] )

m = [ "이순신", 34, "군인" ]

print(m[0])
print(m[1])
# m[0] -> 이름인지, 나이인지, 직업인지 알 수 가 없다.

info = { "name" : "이순신" , "age":20 , "job":"군인"}
print( info["job"] )

# 딕셔너리는 언제 사용하냐?
#   로그인 회원이나, 상품정보, 단일게시글 정보, 설정값
#   JSON데이터, API 응답 데이터용

mem = dict() # 비어있는 딕셔너리

print( info.get("city") )

info["city"] = "대전"  # 딕셔너리에 키와 값 추가

print( info )

# 삭제 (pop, del)
city = info.pop("city") # return이 되기때문에 삭제할 값을 밖으로 꺼내준다.
print( city )
print( info )

del info["age"]
print( info )

# 검색
if "city" in info:       # in - 딕셔너리에서 키 존재 여부 확인
    print("도시 정보 있다")

if "김유신" in info.values(): 
    print("김유신 있다.")

k , v = info.items() # 딕셔너리에서 키와 value 가져오기
info.keys() # 딕셔너리에서 키만 가져오기

print( type(k), type(v) )
print( k, v )

# 딕셔너리에 key로 사용가능한것
#   문자열, 정수, 실수, 튜플

info = {
    "id" : 1004,
    "email" : "hahaha@naver.com",
    "name" : "이순신",
    "birth" : "20010424",
    "address" : "대전 광역시 중구 선화동 방산빌딩 2층 203호"
}

# 이름이 이순신이냐?
if "name" in info:               # 키를 찾고
    if info["name"] == "이순신":  # value를 찾는다
        print("이순신 이다.")
    else:
        print("이순신이 아니다.")
else:
    print("이름 정보가 없다.")

# 이메일의 도메인은 무엇인가?
if "email" in info:
    email = info["email"] # 딕셔너리에서 email키의 값 가져오기
    domain = email[email.index("@")+1:]  # split 보다 슬라이싱이 훨씬 낫다.
    print(domain)
    # domain = email.split("@")[1]
    # print(domain)

# 주소가 잘못 저장 되었다. 선화동 아니고 대흥동이다 수정하시오
if "address" in info:
    addr = info["address"]
    addr = addr.replace("선화동","대흥동") # replace로 선화동 -> 대흥동 으로 바꾸고
    print(addr)
    info["address"] = addr               # address에 addr 값을 다시 넣어줘야한다.

print( info )

# 리스트에 값 넣어주기
nums = []
for i in range(1,5):
    nums.append( i * 2 )
print(nums)

# 컴프리헨션
#   [ 표현식 for 변수 in 반복대상 ]
nums2 = [ i * 2 for i in range(1,5) ]
print(nums2)

# 1~15 까지 숫자중에서 3의 배수만 리스트에 저장하겠다.
nums3 = [ i for i in range(1,16) if i%3 == 0 ]
print(nums3)

cost = [4500, 6700, 3100, 5800, 2700, 4900]
# cost 리스트에는 상품의 가격이 저장 되어 있다.
# 5000원 이하는 저가형 , 5000원 초과는 고가형 상품이라고 저장하시오
# if~else 를 표현식에 쓰는경우
# [ 저장값 if 조건식 else 저장값 for 변수 in 반복대상 ]
result = [ "저가형" if p <= 5000 else "고가형" for p in cost ]
print(result)


# 학생 성적 관리 프로그램 만들기 , 과목, 국어, 수학, 영어
std1 = [ 89, 56, 73 ]
std2 = [ 45, 87, 35 ]
std3 = [ 81, 85, 94 ]
std4 = [ 90, 34, 61 ]
std5 = [ 59, 63, 70 ]
stdName = ["이순신", "임꺽정", "한석봉", "정약용", "김춘추"]

std = std1,std2,std3,std4,std5
print(std)
score = dict()
# 과목명은 튜플
subject = ("국어", "수학", "영어")

for i, name in enumerate(stdName):  # 인덱스로 이름을 가져오고
    temp = dict()
    for k, s in enumerate(std[i]):  # 인덱스로 점수를 가져온다.
        temp[subject[k]] = s
    score[name] = temp

# 한석봉 학생의 성적을 출력하세요
print( score["한석봉"])
for k , v in score["한석봉"].items(): # 한줄에 하나씩 나오게 하는 방법
    print(k,v)

print(score)


# 문제 1. 딕셔너리를 만드세요.
snackName = ["새우깡", "칙촉", "마가렛", "짱구", "포카칩", "초코하임"]
price = [ 2000, 3200, 4500, 3000, 2800, 4200]

snack = dict()
for i, name in enumerate(snackName):
    snack[name] = price[i]

print(snack)

snack2 = { k:price[i] for i, k in enumerate(snackName)}
print(snack2)

# 문제 2. 딕셔너리를 만들고 다음 조건으로 조회하세요
item = ["선풍기","냉장고","에어컨","TV","컴퓨터","노트북","청소기"]
brand = ["LG","삼성","LG","삼성","HP","DELL","다이슨"]
price = [80000, 1250000, 850000, 1540900, 2300000, 1570000, 534000]

# item, brand, price 의 각 인덱스 매칭이다.
#   선풍기는 LG이고 금액은 80000원이다.
# 딕셔너리의 키는 제품명 value는 브랜드와 금액
# 삼성 브랜드의 제품명과 금액을 출력하세요

product = dict()

for i, k in enumerate(item):
    product[k] = {"brand": brand[i], "price": price[i]} 
print(product)

# product = { k:{"brand":brand[i], "price":price[i]}
#             for i, k in enumerate(item)}
# print(product)

for k, v in product.items():
    if v["brand"] == "삼성":
        print(k, v["price"])



# set - 중복 허용하지않고, 순서가 없는 자료형
# 데이터 정리, 검색의 목적으로 많이 사용함.

data = {1,2,3,4,5,3,4,5,6}  # 딕셔너리랑 같은 중괄호이지만 키 없이 값만 넣어준다.
print( data )               # 중복이 되지 않기 때문에 같은 값이 들어가 있으면 덮어쓴다.
set1 = set() # 비어있는 set 만들기

list = ["이순신","김춘추","장영실","이순신","장영실"]
set2 = set(list)
print(set2)
# print(set2[1]) # 인덱스 접근 불가 (순서가 없기 때문)

set2.add("한석봉") # add() 로 set에 값 추가
print(set2)

set2.update( ["정약용","문익점","이성계"]) # update() 로 여러개 값 추가
print(set2)

set2.remove("한석봉") # remove() 로 값 삭제 (※ 존재하지 않은 데이터 삭제 시 오류)
print(set2)

set2.discard("한석보") # discard() remove와 같은 삭제 (값이 존재하지 않아도 오류가 뜨지 않음)
print(set2)

# set안에 값이 존재하냐 -> in

# 교집합, 합집합, 차집합
a = {"복숭아","배","메론","체리","포도"}
b = {"사과","배","딸기","바나나"}
c = {"바나나","참외","사과","귤","포도","딸기","토마토"}

print( a & b ) # 교집합

print( a | c ) # 합집합

print( b - c ) # 차집합

print( c ^ b ) # 대칭 차집합 : 교집합인것 빼고 나머지

for fruit in c:
    print(fruit)

'''
    list - 다수의 데이터 저장용으로 많이 사용, 중복 허용, 추가수정삭제 가능
    tuple - 다수의 데이터 저장 가능, 중복 허용, 추가수정삭제 불가능
    dictionary - key : value 구조 , key는 중복 안됨
    set - 중복 허용하지 않음, 순서 없음, 검색, 그룹(집합)에 사용
'''

# 과일 가게 재고 관리 프로그램

import random

# 과일 데이터
fruits = [
    {"name":"사과", "price":3000, "stock":20},
    {"name":"바나나", "price":1500, "stock":30},
    {"name":"포도", "price":5000, "stock":11},
    {"name":"복숭아", "price":4000, "stock":8},
    {"name":"수박", "price":9900, "stock":34}
]

sales = [] # 판매 기록 용
admin = { "id":"admin", "pw":"1234" } # 관리자 로그인

print("\n========= 과일 재고 관리 프로그램 =========\n")

userId = input("아이디 : ").strip().lower()
userPw = input("비밀번호 : ").strip()

if userId == admin["id"] and userPw == admin["pw"]:
    print("로그인 성공")
else:
    print("아이디 또는 비밀번호가 잘못되었습니다.")
    exit()

# 로그인 후 메뉴 실행
while True:
    print("\n==== 메뉴 ====")
    print("1. 과일 목록 보기")
    print("2. 과일 검색")
    print("3. 과일 판매")
    print("4. 재고 확인")
    print("5. 과일 추천")
    print("6. 판매 기록보기")
    print("0. 종료")

    menu = input("메뉴 선택 : ").strip()

    if menu == "1": # 목록
        for fruit in fruits:
            print(f"{fruit['name']} / 가격: {fruit['price']}원 / 재고: {fruit['stock']}개")

    elif menu == "2": # 검색
        keyword = input("검색어 입력 : ").strip()

        result = [ fruit for fruit in fruits if keyword in fruit["name"] ]
        
        if result :
            for f in result:
                print(f["name"], "/", f["price"],"원 / 재고", f["stock"],"개")
        else:
            print("검색 결과가 없습니다.")

    elif menu == "3": # 판매
        name = input("판매한 과일 이름 : ").strip()
        count = int( input("판매 수량 : ").strip() )
        
        found = False # 판매한 과일이 과일 데이터에 있냐 없냐
        for fruit in fruits:
            if fruit["name"] == name:
                found = True  # 판매하고자 하는 과일이 있다
                if fruit["stock"] >= count:
                    fruit["stock"] -= count  # fruit["stock"] = fruit["stock"]-count 와 같다.
                    sale = ( name , count , fruit["price"]*count) # 판매 내역을 튜플로 생성
                    sales.append(sale)  # 판매기록용 sales에 저장
                    print("판매 완료")
                    print("총 금액 : ", fruit["price"]* count, "원")
                else:
                    print("재고가 부족합니다.")
        
        if not found:  # 과일데이터에서 판매할 과일이 없는 경우 - not 연산자에 의해 False <-> 참
            print("해당 과일이 없습니다.")


    elif menu == "4": # 재고
        # 과일들의 재고량을 확인하여 5개 이하인 과일들 찾아서 출력하기
        # 만약 5개 이하인 과일이 없다면 재고 부족 과일이 없습니다. 라고 출력
        low_stock = [fruit for fruit in fruits if fruit["stock"] <= 5]

        if low_stock:
            for f in low_stock:
                print(f['name'],"/ 재고 : ", f["stock"], "개")
        else:
            print("재고 부족 과일이 없습니다.")

        # low = False
        # for fruit in fruits:
        #     if fruit["stock"] <= 5:
        #         low = True
        #         print(f"{fruit['name']} 재고 부족: {fruit['stock']}개")
        
        # if not low:
        #     print("재고 부족 과일이 없습니다.")


    elif menu == "5": # 추천
        # 오늘의 추천 과일 - 랜덤
        # import random - randint(1,10): 1~`0 사이정수, randrange(1,10) : 1~9 사이 정수
        #   choice(리스트) : 리스트 내분의 값중 하나 선택
        #   choices(리스트, k=3) : 리스트 안에서 3개를 선택(중복허용)
        #   sample(리스트, 4) : 리스트안에 값 중 4개를 선택(중복없음)
        #   shuffle(리스트) : 리스트 안에 값의 순서를 댄덤하게 섞음
        #   choices(리스트, 가중지, k=5) : 리스트안에 값의 확률(가중치)을 적용하여 5개 선택
        # i = [1,2,3,4,5]
        #  w = [0.2, 0.3, 0.2, 0.1, 0.2]
        # choices(i, w, k=3)
        
        # random.seed(10) # 시작점을 10으로 정한다.
        # print( random.randint(1, 100) )
        recommend = random.sample( fruits , 3 )
        # sorted 는 정령될 새로운 리스트 반환된다.
        result = sorted(recommend, key=lambda x : x["name"])

        print("===== 오늘의 추천과일 =====")
        for fruit in result:
            print(f"{fruit['name']}")
        

    elif menu == "6": # 기록
        # 판매 기록을 출력 - sales
        # 판매한 과일에 대해 출력, 총 판매 금액 출력
        print("=== 판매 기록 ===")

        total = 0 # 총판매 금액 저장용

        for sale in sales:
            name, count, price = sale
            print( name, count, "개   ", price,"원")
            total += price  # total = total + price

        print("총 판매 금액 : ",total,"원")

    elif menu == "0":
        print("")
        break
    else:
        print("잘못된 메뉴입니다.")