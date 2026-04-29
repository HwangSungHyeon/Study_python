
# 대전 광역시 자전거 타슈의 위치 현황 파일을 불러오기
# 타슈 자전거 정거장 위치 찾기 만들기
#   동 이름 또는 현재 위치(건물, 지명 등) 입력받기
# 검색어가 포함되어있는 정거장 이름 또는 주소에서 찾기

# 조회한 전체 정거장을 출력하는데 중복 없어야 되고
#   정거장 명 기준 내림차순으로 정렬 하기

import csv

station_list = []

with open("file/타슈.csv", "r") as f:
    data = csv.DictReader(f)

    for row in data:
        station_list.append(row)

keyword = input("동 이름 또는 현재 위치 입력 : ")
result = set()

for row in station_list:
    for k, v in row.items():
        if k in ["스테이션_ 성명(Station)", "위치"]:
            if keyword in v:
                result.add(row["스테이션_ 성명(Station)"])

print(sorted(result, reverse=True))
