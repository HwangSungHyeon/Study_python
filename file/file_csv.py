# csv - 쉼표로 구분된 데이터

import csv

# with open("file/test1.csv", "r" , encoding="utf-8") as f:
#     data = csv.reader(f)
#     print( data )
#     header = next(data)
#     print( header )
#     # row는 ,기준으로 잘라서 리스트형태로 보여준다.
#     for row in data:
#         print(row)

# with open("file/test2.csv", "a", newline="", encoding="utf-8") as f:  # newline="" 를 넣으면 줄 사이의 공백을 없앨 수 있다.
#     w = csv.writer(f)
#     w.writerow(["이순신","19960522","010-5678-4567"])

# 딕셔너리로 표현하는 방법
# with open("file/test2.csv", "r", encoding="utf-8") as f:
#     dic = csv.DictReader(f)

#     for row in dic:
#         print(row)

header = ["이름","나이","직업"]
with open("file/test2.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=header)
    w.writeheader()
    w.writerow( {"이름":"문익점", "나이":34, "직업":"산업스파이"} )
    w.writerow( {"이름":"정약용", "나이":45, "직업":"발명가"} )
