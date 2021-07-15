# 자료형의 값을 저장하는 공간, 변수

# 변수 이름 = 변수에 저장할 값

# a = 1
# b = "python"
# c = [1, 2, 3]

# print(a, b, c)

# 변수란?
a = [1, 2, 3]
print(id(a))

# 리스트를 복사할 때
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))

print(a is b)

a [1] = 4
print(a)
print(b)

# 1. [:]사용
a = [1, 2, 3]
b = a[:] # 리스트 a의 처음 요소부터 끝 요소까지 슬라이싱
a[1] = 4
print(a)
print(b)

# 2. copy 모듈 사용
from copy import copy
a = [1, 2, 3]
b = copy(a)

print(a)
print(b)

print(b is a)

# 변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
print(a, b)

(a,b) = 'python', 'life' # 튜플
print(a, b)

[a,b] = ['Python', 'life'] # 리스트
print(a,b)

a = b = 'Python' # 여러 개의 변수에 같은 값 대입
print(a, b)

a = 3
b = 5
a, b = b, a # a와 b의 값을 바꿈
print(a)
print(b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)