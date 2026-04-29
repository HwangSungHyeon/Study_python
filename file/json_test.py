
import json

info = [
    {
        "name":"김유신",
        "age":35,
        "addr":"경주"
    },
    { 
        "name":"이순신",
        "age":50,
        "addr":"여수"
    }
]

# json 쓰기 (dump)
with open("file/info.json", "w" , encoding="utf-8") as f:
    json.dump(info , f, ensure_ascii=False, indent=4) # ensure_ascii=False 을 써야 한글이 잘나온다. , indent=4 -> 4칸 들여쓰기라는 뜻


# json 읽기 (load)
with open("file/info.json", "r", encoding="utf-8") as f:
    member = json.load(f)

for i in member:
    print(i["name"], i["age"])

# json 추가 하는 법 -  읽기 -> append로 member에 저장 -> 쓰기
member.append( {"name":"문익점","age":25,"addr":"개경"} )

with open("file/info.json", "w" , encoding="utf-8") as f:
    json.dump(member, f, ensure_ascii=False, indent=4)


"""
    파이썬  과   json
    dict    -   object
    list    -   array
    str     -   string
    int,float   -   number
    True    -   true
    False   -   false
    None    -   null
    
"""
