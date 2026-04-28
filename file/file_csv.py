# csv - 쉼표로 구분된 데이터

import csv

with open("file/test1.csv", "r" , encoding="utf-8") as f:
    data = csv.reader(f)
    print( data )

    # row는 ,기준으로 잘라서 리스트형태로 보여준다.
    for row in data:
        print(row)