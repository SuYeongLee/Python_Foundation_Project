# 모듈

# 모듈 만든 파일명
# mod1.py

# 모듈 불러오기
import mod1
print(mod1.add(3, 4))
print(mod1.sub(4, 2))

# import 모듈이름

# from 모듈이름 import 모듈 함수

# from mod1 import add
# print(add(3, 4))

# from mod1 import add,sub

# print(add(4, 5))
# print(sub(7, 2))

from mod1 import*

print(add(4, 5))
print(sub(5, 2))

