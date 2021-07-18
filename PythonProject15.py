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

    def add(self, numa, numb):
        self.result = numa + numb
        return self.result
    
    def mul(self, numa, numb):
        self.result = numa * numb
        return self.result

    def sub(self, numa, numb):
        self.result = numa - numb
        return self.result

    def div(self, numa, numb):
        self.result = numa / numb
        return self.result

a = FourCal()

print(a.add(4, 2))
print(a.sub(4, 2))
print(a.mul(4, 2))
print(int(a.div(4, 2)))

# 1. 객체에 숫자 지정할 수 있게 만들기

# def 함수 이름(매개변수):
#    수행할 문장


# 메소드의 또 다른 호출 방법
a = FourCal()
FourCal.setdata(a, 4, 2)

a = FourCal()
a.setdata(4, 2)

def setdata(self, first, second):
    self.first = first
    self.econd = second


a = FourCal()
a.setdata(4, 2)
print(a.first)
print(a.second)

a = FourCal()
b = FourCal()

a.setdata(4, 2)
print(a.first)

b.setdata(3, 7)
print(b.first)

print(a.first)

a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)
print(id(a.first)) # a의 first 주소 값을 확인
print(id(b.first)) # b의 first 주소 값을 확인


# 1. 더하기 기능 만들기

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result


a = FourCal()
a.setdata(4, 2)
print(a.add())