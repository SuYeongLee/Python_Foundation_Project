# 내장 함수

# abs => 절대값
# abs(x)는 어떤 숫자를 입력받아씅ㄹ 때, 그 숫자의 절대값을 돌려주는 함수

# print(abs(3))

# print(abs(-3))

# print(abs(-1.2))

# all => 모두 참인지 검사
# all(x)는 반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 True.
# 거짓이 하나라도 있으면 False를 돌려준다.

# print(all([1,2,3]))

# print(all([1,2,3,0]))

# any => 하나라도 참인가?
# any(x)는 x중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False를 돌려준다.
# all(x)의 반대

# print(any([1,2,3,0]))

# print(any([0, ""]))

# chr => 아스키코드를 입력받아 문자 출력
# chr(i)는 아스키(ASCII)코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
# chr(십진법)

# print(chr(97)) # 아스키 코드 97은 소문자 a
# print(chr(48)) # 아스키 코드 48은 숫자 0

# dir => 몫과 나머지를 튜플 형태로 돌려줌
# dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다.
# 다음 예는 리스트와 딕셔너리 객체 관련 함수(메서드)를 보여 주는 예

# print(dir([1, 2, 3]))
# print(dir({'1':'a'}))

# divmod => 몫과 나머지를 튜플 형태로 돌려줌
# divmod(a, b)는 2개의 숫자를 입력으로 받는다.
# a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수이다.
# print(divmod(7, 3)) # 7 나누기 3의 몫은 2, 나머지는 1

# print(7 // 3)
# print(7 % 3)

# enumerate => 열거하다
# enumerate는 '열거하다'라는 뜻이다. 
# 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 
# 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.

# i -> index, name
# for i, name in enumerate(['body', 'foo', 'bar']):
#     print(i, name)

# eval => 실행 후 결과값을 돌려줌
# eval(expression)은 실행 가능한 문자열(1 + 2, 'hi' + 'a' 같은 것)을 입력으로
# 받아 문자열을 실행한 결괏값을 돌려주는 함수

# print(eval('1+2'))

# print(eval("'hi' + 'a'"))

# print(eval('divmod(4,3)'))

# filter => 함수를 통과하여 참인 것만 돌려줌
def positive(l):
    result = [] # 반환 값이 참인 것만 걸러내서 저장할 변수
    for i in l:
        if i > 0: # i가 0보다 클 때
            result.append(i) # 리스트에 i 추가
    return result

print(positive([1, -3, 2, 0, -5, 6]))

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

# hex
# hex(x)는 정수 값을 입력받아 16진수(hexadecimal)로 변환하여 돌려주는 함수

print(hex(234))
print(hex(3))

# id => 10진수 정수 형태로 변환
# id(object)는 객체를 입력받아 객체의 고유 주소 값(레퍼런스)을 돌려주는 함수이다.

a = 3

# 3, a, b는 모두 같은 객체를 가리킴
print(id(3))
print(id(a))
b = a
print(id(b))
print(id(4))

# input => 사용자 입력 받는 함수
# input([prompt])은 사용자 입력을 받는 함수이다.

# a = input() # 사용자가 입력한 정보를 변수 a에 저장
# print(a)
# b = input("Enter: ") # Enter: 프롬프트를 띄우고 사용자 입력을 받음
# print(b)

# int => 10진수 정수 형태로 변환
# int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려줌

print(int('3')) # 문자열 형태 '3'
print(int(3.4)) # 소수점이 있는 숫자 3.4
print(int('11', 2))

# 16진수로 표현된 1A의 10진수 값은 다음과 같이 구한다.
print(int('1A', 16))

# isinstance
# isinstance(object, class)는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
# 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.

class Person: pass # 아무 기능이 없는 Person 클래스 생성

a = Person() # Person 클래스의 인스턴스 a 생성
print(isinstance(a, Person)) # a가 Person 클래스의 인스턴스인지 확인

b = 3
print(isinstance(b, Person))

# len => 길이
# len(s)은 입력값 s의 길이(요소의 전체 개수)를 돌려주는 함수
print(len("python"))
print(len([1,2,3]))
print(len((1, 'a')))

# list => 리스트로 변환
# list(s)는 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수이다.
print(list("python"))
print(list((1,2,3)))

# map => 각 요소가 수행한 결과를 돌려줌
# map(f, iterable)은 함수(f)와 반복 가능한(iterable)자료형을 입력으로 받는다.
# map은 입력 받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수

def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

result = two_times([1, 2, 3, 4])
print(result)