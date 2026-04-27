# 다른 파일에 있는 함수를 가져올 수 있다.

import calc

print( calc.add(10,20) )

# 다른 파일의 이름이 너무 길 경우 as를 사용해 별명을 만들어 넣을 수 있다.
import calc as c
print( c.add(20,20) )

# import calc 는 calc.py 전체사용

# 특정 함수나 변수를 사용하고자 한다면 아래와 같이 하면된다.
from calc import add
print(add(10,10))

# from calc import *  <- 이 방식은 잘 쓰지않는다.