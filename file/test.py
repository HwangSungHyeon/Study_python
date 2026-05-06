# 파일 입출력 - 프로그램에서 생성된 데이터들은 프로그램 종료시 메모리에서 사라진다.
#   필요한 데이터들을 남겨두기 위해서는 파일로 저장을 해야한다.
#   파일 입출력은 데이터를 저장하고 불러오는 방법이다.

# 파일쓰기 - 저장 , 파일 읽기 - 불러오기

#open("파일명", "모드")  모드 - r : 읽기 , w : 쓰기(덮어쓰기), a : 추가

# 쓰기("w")

# f = open("file/test1.txt", "w" , encoding="utf-8") # 앞에 변수를 만들어줘야 쓸 수 있다.
# f.write("안녕하세요")
# f.close() # 여러군데에서 작업하면 문제가 생기므로 항상 닫아야한다.

# 자동으로 닫아주는 방식(with)
# text = input("아무거나 입력 : ")
# with open("file/test1.txt", "w" , encoding="utf-8") as f:
#     f.write(text)

# 점심 = ["돈가스", "짜장면","탕수육","떡볶이","감자탕"]

# with open("file/test2.txt", "w" , encoding="utf-8") as f:
#     for 밥 in 점심:
#         f.write(밥+"\n")

# 점심 = []


# 읽기("r")

# with open("file/test2.txt", "r", encoding="utf-8") as f:
#    f.read()

# with open("file/test2.txt", "r", encoding="utf-8") as f:
#    f.readline()

# with open("file/test2.txt", "r", encoding="utf-8") as f:
#    f.readlines()

# 한줄에 하나씩 읽는 방법
# with open("file/test2.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         점심.append(line[:line.index("\n")]) # 점심.append(line.replace(",",""))
# print(점심)


# 추가("a")
# with open("file/test2.txt", "a", encoding="utf-8") as f:
#     f.write("라면")

# 새로운 파일 추가
# with open("file/test3.txt", "a", encoding="utf-8") as f:
#     f.write("새파일")

# with open("file/2.jpg", "rb") as f:
#     img = f.read()
# print(img)

# 문제 1. input 함수로 입력받은 값을 note.txt에 저장하시오

# user = input("입력 : ")
# with open("file/note.txt", "w", encoding="utf-8") as f:
#     f.write(user)

# 문제 2. 회원가입을 받아서 파일로 저장하세요
#   회원 정보는 이름, 이메일, 비밀번호, 나이
#   파일 이름은 회원의 이메일 @ 앞부분이 파일 이름입니다.
# 파일 형식은 txt 입니다.

name = input("이름 : ")
email = input("이메일 : ")
pw = input("비밀번호 : ")
age = input("나이 : ")
file_name = "file/"+email.split("@")[0]+".txt"

with open(file_name, "w", encoding="utf-8") as f:
    f.write(f"이름 : {name}\n이메일 : {email}\n비밀번호 : {pw}\n나이 : {age}" )
