# 클래스

result = 0

def add(num):
    global result
    result += num # result = result + num
    return result

print(add(3))
print(add(4))

result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))

print(cal2.add(3))
print(cal2.add(7))

print(cal1.sub(3))
print(cal1.sub(2))

# 과자 틀 -> 클래스(class)
# 과자 틀을 사용해 만든 과자 -> 객체(object)

class Cookie:
    pass

a = Cookie()
b = Cookie()


class FourCal:
    pass

a = FourCal()
print(type(a))

# 객체에 숫자 지정할 수 있게 만들기

class FourCal:
    def setdata(self, first, second): # 1번 메서드의 매개변수
        self.first = first  # 2번 매서드의 수행문
        self.second = second

    def add(self):
        self.result = self.first + self.second
        return self.result
    
    def mul(self):
        self.result = self.first * self.second
        return self.result

    def sub(self):
        self.result = self.first - self.second
        return self.result

    def div(self):
        self.result = self.first / self.second
        return self.result

a = FourCal()
a.setdata(4, 2)

print(a.add())
print(a.mul())
print(a.sub())
print(int(a.div()))


# 클래스 구조 만들기

# class FourCal:
#     pass

# a = FourCal()
# print(type(a))

# 객체에 숫자 지정할 수 있게 만들기

# a.setdata(4, 2)

# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

# def 함수 이름(매개변수):
#    수행할 문장

# def setdata(self, first, second): # (1) 메서드의 매개변수
    # (2) 메서드의 수행문
#    self.first = first
#    self.second = second

# (1)setdata 메서드의 매개변수
# a = FourCal()
# a.setdata(4, 2)

# 메서드의 또 다른 호출 방법

# a = FourCal()
# FourCal.setdata(a, 4, 2)

# a = FourCal()
# a.setdata(4, 2)

# (2)setdata 메서드의 수행문

# def setdata(self, first, second): # (1) 메서드의 매개변수
    # (2) 메서드의 수행문
    # self.first = first
    # self.second = second

# self.first = 4
# self.second = 2

# a.first = 4
# a.second = 2

# a = FourCal()
# a.setdata(4, 2)
# print(a.first)
# print(a.second)

# a = FourCal()
# b = FourCal()

# a.setdata(4, 2)
# print(a.first)

# b.setdata(3, 7)
# print(b.first)

# print(a.first)

# a = FourCal()
# b = FourCal()
# a.setdata(4, 2)
# b.setdata(3, 7)
# print(id(a.first)) # a의 first 주소 값을 확인
# print(id(b.first)) # b의 first 주소 값을 확인

# 더하기 기능 만들기

# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result

# a = FourCal()
# a.setdata(4, 2)
# print(a.add())

# 곱하기, 빼기, 나누기 기능 만들기
# class FourCal:
#     def setdata(self, first, second):
#         self.first = first
#         self.second = second
#     def mul(self):
#         result = self.first * self.second
#         return result
#     def sub(self):
#         result = self.first - self.second
#         return result
#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal()
# a.setdata(4, 2)
# print(a.mul())
# print(a.sub())
# print(a.div())

a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(3, 8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())

# 생성자(Constructor)

# a = FourCal()
# print(a.add())

class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

a = FourCal(4, 2)

# 매개 변수
# self, first, second

# 값
# 생성되는 객체, 4, 2

print(a.first)
print(a.second)

a = FourCal(4, 2)
print(a.add())
print(a.div())

# 클래스의 상속
# class 클래스 이름(상속할 클래스 이름)
class MoreFourCal(FourCal):
    pass

a = MoreFourCal(4, 2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
print(a.pow())

# 메서드 오버라이딩

# a = FourCal(4, 0)
# a.div()

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0: # 나누는 값인 0인 경우 숫자 0을 돌려주도록 수정
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.div())

# 클래스 변수

class Family:
    lastname = "김"

print(Family.lastname)

a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = "박"
print(a.lastname)
print(b.lastname)

# 모든 같은 메모리를 가리키고 있음

print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))