# 함수

# 파이썬 함수의 구조

# def 함수 이름(매개변수):
#   수행할 문장1
#   수행할 문장2

# def add(a, b):
#     return a + b

# a = 3
# b = 4
# c = add(a,b)
# print(c)

# 매개 변수와 인수

# def add(a, b): # a, b는 매개변수
#     return a + b
# print(add(3, 4)) # 3, 4는 인수

# 입력값과 결괏값에 따른 함수의 형태

# 일반적인 함수

# def 함수 이름(매개변수):
#   수행할 문장
#   ...
#   return 결괏값

# def add(a, b):
#     result = a + b
#     return result # a + b의 결괏값 반환

# a = add(3, 4)
# print(a)

# 입력값이 없는 함수
# def say():
#     return 'HI'

# a = say()
# print(a)

# 결괏값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다."% (a, b, a+b))

add(3, 4)
a = add(3, 4)
print(a)

# 입력값도 결과값도 없는 함수
def say():
    print('HI')

say()

# 함수이름()

# 매개변수 지정하여 호출하기
def add(a, b):
    return a+b

result = add (a = 3, b = 7) # a에 3, b에 7을 전달
print(result)

result = add(b = 5,a = 3) # b에 5, a에 3을 전달
print(result)


# def 함수이름(*매개변수):
#    수행할 문장


# 여러 개의 입력값을 받는 함수 만들기

def add_many(*args):
    result = 0
    for i in args:
        result = result + i # *args에 입력받은 모든 값을 더한다.
    return result

result = add_many(1, 2, 3)
print(result)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)

def add_mul(choice, *args):
    if choice == "add": # 매개변수 choice에 'add'를 입력받았을 때
        result = 0
        for i in args:
            result = result + i # args에 입력받은 모든 값을 더한다.
    elif choice == "mul": # 매개변수 choice에 'mul'을 입력받았을 때
        result = 1
        for i in args:
            result = result * i # *args에 입력받은 모든 값을 곱한다.
    return result

# 'add' +사용 
result = add_mul('add', 1,2,3,4,5)
print(result)

# 'mul' *사용
result = add_mul('mul', 1,2,3,4,5)
print(result)

# 키워드 파라미터
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1)
print_kwargs(name= 'foo', age=3)

# 함수의 결괏값은 언제나 하나이다

def add_and_mul(a,b):
    return a+b, a*b # 2개의 매개변수를 받아 더한 값과 곱한 값을 돌려준다.

result = add_and_mul(3, 4)
result = (7, 12)
result1, result2 = add_and_mul(3, 4)

def add_and_mul(a,b):
    return a+b
    return a*b

result = add_and_mul(2, 3)
print(result)

# return의 또 다른 쓰임새
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s입니다." %nick)

say_nick('야호')
say_nick('바보')

def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)
say_myself("박응용", 27, True)
say_myself("박응용", 27, False)

# def say_myself(name, man=True, old):
#     print("나의 이름은 %s입니다." % name)
#     print("나의 이름은 %s입니다." % old)
#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

say_myself("박으용", 27)

# vartest.py
a = 1 # 함수 밖의 변수 a
def vartest(a):
    a = a + 1

vartest(a)
print(a) # a값 출력

def vartest(hello):
    hello = hello + 1

# 함수 안에서 선언한 변수의 효력 범위

# vartest_error.py
def vartest(a):
    a = a + 1

vartest(3)
print(a)

# 함수 안에서 함수 밖의 변수를 변경하는 방법

# 1. return 사용하기 (추천)
# vartest_return.py
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

# 2. global 명령어 사용하기 (권장 안함)
# vartest_global.py
a = 1
def vartest():
    global a
    a = a + 1

vartest()
print(a)

# lambda
# lambda 매개변수1, 매개변수2, : 매개변수를 사용한 표현식
add = lambda a, b: a+b
result = add(3, 4)
print(result)