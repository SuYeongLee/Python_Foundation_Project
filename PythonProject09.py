# if문

# if문 기본 구조

# if 조건문:
#   수행할 문장1
#   수행할 문장2
# else:
#   수행할 문장A
#   수행할 문장B

# money = True

# if money:
#     print("택시를 타고 가라")
# else:
#     print("걸어 가라")

# 들여쓰기
# money = True
# if money:                 # 조건문
#     print("택시를")       # 수행할 문장1
#     print("타고")         # 수행할 문장2
#         print("가라")     # 수행할 문장3

# 조건문이란 무엇인가?
meoney = True
if meoney:
    print(meoney)

# x < y : x가 y보다 작다
# x > y : x는 y보다 크다.
# x == y : x와 y는 같다
# x != y : x와 y는 같지 않다.
# x >= y : x와 y는 크거나 같다.
# x <= y : x와 y는 작거나 같다.

x = 3
y = 2
print(x > y) # <- 3>2 True
print(x < y) # <- 3<2 False
print(x == y) # <- 3 == 2 False
print(x != y) # <- 3 != 2 True

money = 2000 # <- 2000원을 가지고 있다.

if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# and, or, not
# x or y : x와 y 둘 중에 하나만 참이어도 참이다.
# x and y : x와 y 모두 참이어야 참이다.
# not x : x가 거짓이면 참이다.

money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# x in s, x not in s
# in : not in
# x in 리스트 : x not in 리스트
# x in 튜플 : x not in 튜플
# x in 문자열 : x not in 문자열