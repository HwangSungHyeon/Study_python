# 1
# student = ("이영희", 22, "컴퓨터공학")

# name , age , major = student
# print(name,age,major)

# 2
# info = {"이름":"김철수","나이":25,"도시":"부산","직업":"디자이너"}
# for k, v in info.items():
#     print(k,v)

# 3
# scores = [
#     ("국어",85),
#     ("수학",92),
#     ("영어",78)
# ]

# total = 0
# for 과목 , 점수 in scores:
#     total += 점수
# print(f"평균 : {total/len(scores)}")

# 4
# people = [
#     {"name": "홍길동", "age": 30},
#     {"name": "김철수", "age": 25},
#     {"name": "이영희", "age": 28},
# ]
# peoples = [i for i in people if i["age"] >= 27]
# for i in peoples:
#     print(f"이름 : {i['name']}")

# 5
import csv
with open("file/people.csv", "r", encoding="utf-8") as f:
    header = csv.reader(f)
    head = next(header)
    print(" | ".join(head))
    for i in header:
        name , age , city = i
        if city == "서울":
            print(f"{name} - {age} - {city}")

total = 0
with open("file/people.csv", "r", encoding="utf-8") as f:
    data = csv.reader(f)
    next(data)
    for i in data:
        name , age , city = i
        total += int(age)
print(total)
        

import csv
with open("file/people.csv", "r", encoding="utf-8") as f:
    data = csv.reader(f)
    next(data)
    for i in data:
        name , age , city = i
        if name.startswith("최") and len(name) == 3:
            print(f"{name} - {age} - {city}")




