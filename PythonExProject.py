# 연습문제함

# 112 ~ 115P
# 2장 - 파이썬 프로그래밍의 기초, 자료형

# 1번 문제
# a = 80
# b = 75
# c = 55
# print((a + b + c)/3) # 70.0

# 2번 문제
# print(1 % 2) #1
# print(2 % 2) #0
# print(3 % 2) #1
# print(4 % 2) #0

# 3번 문제
# pin = "881120-1068234"
# yyyymmdd = pin[:6] # 처음부터 6까지
# num = pin[7:] # 7부터 끝까지
# print(yyyymmdd) # 881120 출력
# print(num) # 1068234 출력

# 4번 문제
# pin = "881120-1068234"
# print(pin[7]) # 1번 남자 2번 여자

# 5번 문제
# a = "a:b:c:d"
# b = a.replace(":", "#") # : -> #로 변경
# print(b) # a#b#c#d

# 6번 문제
# a = [1, 3, 5, 4, 2]
# a.sort() # 정렬
# a.reverse() # 뒤집기
# print(a) # [5, 4, 3, 2, 1]

# 7번 문제
# a = ['Life', 'is', 'too', 'short'] # a변수에 문자 저장
# result = " ".join(a) # result값에 join 문장 합침
# print(result)

# 8번 문제
# a = (1, 2, 3)
# a = a + (4,)
# print(a) # (1, 2, 3, 4) 출력

# a = (1, 2, 3)
# print(id(a)) # a의 고유 주소 값 출력
# a = a + (4,)
# print(a)
# print(id(a)) # (4,) 값이 더해 진 후 a의 고유 주소 값 출력

# 9번 문제

# a[[1]] = 'python'

# 10번 문제

# a = {'A':90, 'B':80, 'C':70}
# result = a.pop('B')
# print(a) # {'A':90, 'C':70}출력
# print(result) # 80 출력

# 11번 문제
# a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# aSet = set(a) # a 리스트를 집합자료형으로 변환
# b = list(aSet) # 집합자료형을 리스트 자료형으로 다시 변환
# print(b) # [1,2,3,4,5] 출력

# 12번 문제
# [1, 4, 3]이 출력된다. 
# a와 b변수는 모두 동일한 [1,2,3]이라는 리스트 객체를 가리키고 있기 때문

# 146P ~ 148P

# 1번 문제

# 첫 번째 조건 : "wife"라는 단어는 a문자열에 없으므로 거짓이다.
# 두 번째 조건 : "python"이라는 단어는 a 문자열에 있지만 "you" 역시 a 문자열에 있으므로 거짓이다.
# 셋 번째 조건 : "shirt"라는 단어가 a 문자열에 없으므로 참이다.
# 네 번재 조건 : "need"라는 단어가 a 문자열에 있으므로 참이다.

# 가장 먼저 참이 되는 것이 세 번째 조건이므로 "shirt"가 출력된다.

# 2번 문제

# result = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
#         result += i
#     i += 1

# print(result) # 166833 출력

# 3번 문제
i = 0
# while True:
#     i += 1 # while문 수행 시 1씩 증가
#     if i > 5: break # i 값이 5보다 크면 while문을 벗어난다.
#     print('*' * i) # i 값 개수만큼 *를 출력한다.

# 4번 문제
# for i in range(1, 101):
#     print(i)

# 5번 문제
# A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
# total = 0
# for score in A:
#     total += score # A학급의 정수를 모두 더한다.
# average = total / len(A) # 평균을 구하기 위해 총 점수를 총 학생수로 나눈다.
# print(average) # 평균 79.0이 출력된다.

# 6번 문제
# numbers = [1, 2, 3, 4, 5]

# result = []
# for n in numbers:
#     if n % 2 == 1:
#         result.append(n*2)

# numbers = [1, 2, 3, 4, 5]
# result = [n*2 for n in numbers if n %2 == 1]
# print(result)

# if 'card' not in pocket:
#     print("걸어 가라")
# else:
#     print("버스를 타고 가라")

# a = 0
# while a < 10:
#     a = a + 1
#     if a % 3 == 0: continue
#     print(a)

# a = 0
# for i in range(1, 101):
#     a += i

# print(a)

# 179p ~ 181p

# 1번 문제

# def is_odd(number):
#     if number % 2 == 1: # 2로 나누었을 때 나머지가 1이면 홀수이다.
#         return True
#     else:
#         return False

# print(is_odd(3))
# print(is_odd(4))

# # 람다와 조건부 표현식을 사용하면 다음과 같이 간단하게도 만들 수 있다.
# is_odd = lambda x: True if x % 2 == 1 else False
# print(is_odd(3))

# 2번 문제

# def avg_numbers(*args): # 입력 개수에 상관없이 사용하기 위해 *args를 사용
#     result = 0
#     for i in args:
#         result += i
#     return result / len(args)

# print(avg_numbers(1, 2))

# print(avg_numbers(1,2,3,4,5))

# 3번 문제
# input1 = input("첫 번째 숫자를 입력하세요:")
# input2 = input("두 번째 숫자를 입력하세요:")

# total = int(input1) + int(input2) # 입력은 항상 문자열이므로 숫자로 바꾸어 주어야 한다.
# print("두수의 합은 %s 입니다." % total)

# 4번 문제

print("you" "need" "python")
print("you" + "need" + "python")
print("you", "need", "python") # 콤마가 있는 경우 공백이 삽입되어 더해진다.
print("".join(["you", "need", "python"]))

# 5번 문제

# f1 = open("test.txt", 'w')
# f1.write("Life is too short!")
# f1.close() # 열린 파일 객체를 닫는다.

# f2 = open("test.txt", 'w')
# print(f2.read())
# f2.close()

# with open("test.txt", 'w') as f1:
#     f1.write("Life is too short!")
# with open("test.txt", 'r') as f2:
#     print(f2.read())

# 6번 문제
# user_input = input("저장할 내용을 입력하세요:")
# f = open('test.txt', 'a') # 내용을 추가하기 위해서 'a'를 사용
# f.write(user_input)
# f.write("\n") # 입력도니 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자 삽입
# f.close()

# 7번 문제
# f = open('test.txt', 'r')
# body = f.read()
# f.close()

# body = body.replace('java', 'python')

# f = open('test.txt', 'w')
# f.write(body)
# f.close()

# f = open("C:/CodeProject/Python_Foundation_Project/test.txt", 'w')
# f.close()

# 262 ~ 265P

# 1번 문제

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)


# 2번 문제

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value) # 100 출력

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

# 3번 문제

print(all([1, 2, abs(-3)-3]))
print(chr(ord('a')) == 'a')

# 4번 문제

print(list(filter(lambda x:x>0, [1,-2, 3, -5, 8, -3])))

# 5번 문제

print(hex(234))
print(int('0xea', 16)) # 16진수 문자열을 10진수로 변경

# 6번 문제

print(list(map(lambda x:x*3, [1,2,3,4])))

# 7번 문제

a = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(a) + min(a))

# 8번 문제

print(17 / 3)
print(round(17 / 3, 4))

# 9번 문제

import sys

numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력

result = 0
for number in numbers:
    result += int(number)
print(result)

# 10번 문제

import os
os.chdir("C:/CodeProject/Python_Foundation_Project")
result = os.popen("dir")
print(result.read())

# 11번 문제

import glob 
glob.glob("C:/CodeProject/Python_Foundation_Project/*.py")

# 12번 문제

import time
print(time.strftime("%Y/%m/%d %H:%M:%S"))

# 13번 문제

import random

result = []
while len(result) < 6:
    num = random.randint(1, 45) # 1부터 45까지의 난수 발생
    if num not in result:
        result.append(num)

print(result)