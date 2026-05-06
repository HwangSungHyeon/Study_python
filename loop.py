# print("숫자 : 1")
# print("숫자 : 2")
# print("숫자 : 3")
# print("숫자 : 4")
# print("숫자 : 5")

# 5번 반복하는 반목문
# for i in range(1, 6, 2): # range(1, 6) -> 1부터 5까지 , range(1, 6, 2) -> 1부터 5까지 2씩 증가
#     print("숫자 : " + str(i))

# print("======================")

# for i in range(5, 1, -1): # range(5, 1) -> 5부터 2까지 , range(5, 1, -1) -> 5부터 2까지 1씩 감소
#     print("숫자 : " + str(i))

# print("======================")

# for ch in "hello":
#     print(ch)

# for name in ["차도헌", "박지연", "이성찬", "김진숙", "이동렬", "김현규"]:
#     if name.startswith("이"):
#         print(name)

# 문제1. - 1부터 10까지의 총합을 구하세요. 반복문을 사용해서
# sum = 0
# for i in range(1,11):
#     sum += i
# print(f"총합 : {sum}")

# 문제2. - ["15,000", "13,000", "8,700", "9,000", "25,000"]
# 배열에 출금 금액들이 저장되어있다.
# 만원 이상 금액들에 대해 출력하세요.

# money = ["15,000", "13,000", "8,700", "9,000", "25,000"]
# for m in money:
#     if int(m.replace(",","")) >= 10000:
#         print(f"출금 금액 : {m}")

# for i in range( len(money)):
#     print("금액 : ", i+1, money[i])

# for i, v in enumerate(money): # 인덱스와 값을 동시에 가져온다.
#     print(i, v)

# 문제3. - [89, 56, 78, 92, 61, 96, 83, 74]
# 203호 학생들의 성적이다. 성적의 총합과 평균을 출력하세요.
# 80점 이상인 학생들의 위치(인덱스)도 출력하세요.
# scores = [89, 56, 78, 92, 61, 96, 83, 74]
# total = 0
# for i, s in enumerate(scores):
#     total += s
#     if s >= 80:
#         print("80점 이상의 학생들의 위치 : ", i,",","점수 : ", s)
# print("총점 :",total)
# print("평균 :",total/len(scores))


# 반복문 while

# while 조건:
#     실행코드

# while문은 조건식이 참인경우에 동작하기 때문에
# 쉽게 무한루프에 들어갈 수 있다.
# 하여 while문  사용시 중단시킬 수 있는 break를 같이 사용하는게 좋다.

# num = 5
# while num > 2:
#     print("2보다 크다")
#     break

# while True: # True를 쓰면 무조건 참이된다.
#     num += 1 # num = num + 1
#     if num == 7: continue # 건너뛰기
#     print(num)
#     if num == 10: break # if문 단독으로 사용 불가

# print("=======================")
# while True:
#     cmd = input("명령어 입력 : ")
#     if cmd == "history":
#         print("모든 기록 출력")
#     elif cmd == "mkdir":
#         print("새로운 폴더 만들기")
#     elif cmd == "remove":
#         print("파일 삭제")
#     elif cmd == "exit":
#         print("종료")
#         break
#     else:
#         print("존재하지 않는 명령어 입니다.")


# 파이썬 랜덤 사용
import random

# num = random.randint(1, 10) # 1~10
# print( num )

# # 동전 앞면 뒷면 맞추기 게임 만들기
# coin = random.randint(1, 2)
# guess = int(input("1. 앞면, 2. 뒷면 : "))
# if coin == guess:
#     print("맞췄습니다!")
# else:
#     print("틀렸습니다.")

n = random.randrange(1, 10) # 1~9

# print(n)


def compare(a,b):
    if a > b: return 1
    elif a < b: return -1
    else: return 0
# 가위바위보 게임 5판 진행
#  5번째 게임이 끝나면 몇승 몇패 몇무인지 출력

game = ["가위", "바위", "보"]
win = lose = draw = 0
for i in range(5):
    com = random.choice(game)
    user = input("가위, 바위, 보 : ").strip()

    print("컴퓨터 : ", com, "나 : ", user)
    # 승 패 무 판단
    # game.index("가위") # 0 , game.index("바위") # 1 , game.index("보") # 2
    # 사전적 순서 비교. 방법은 비교연산자
    cidx = game.index(com)
    uidx = game.index(user)

    comp = cidx - uidx # 유저와 컴의 가위바위보 값 비교
    # 가위-0 바위-1 보-2 -> 유저가 0 컴이 1이라면 컴의 승
    # 즉 comp에 1이 있다면 컴의 승
    if user == com:
        print("무승부")
        draw += 1
    elif comp == -1 or comp == 2:
        print("나의 승")
        win += 1
    else:
        print("나의 패")
        lose += 1
print("승 : ", win, "패 : ", lose, "무 : ", draw)