
"""
fram_12.json 에서 사람을 찾고 사람의 좌표를 출력하세요
"""
import json

with open("file/18396595_frame_12.json", "r", encoding="utf-8") as f:
    data = json.load(f)

anno = data["frames"]["annotations"]

for ann in anno:
    if ann["category"]["code"] == "person":
        anno_value = ann["label"]["x"], ann["label"]["y"]
print("사람의 좌표 : ", anno_value)