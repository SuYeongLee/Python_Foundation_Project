# 연습문제함

# 112 ~ 113P
# 2장 - 파이썬 프로그래밍의 기초, 자료형

# 1번 문제
a = 80
b = 75
c = 55
print((a + b + c)/3) # 70.0

# 2번 문제
print(1 % 2) #1
print(2 % 2) #0
print(3 % 2) #1
print(4 % 2) #0

# 3번 문제
pin = "881120-1068234"
yyyymmdd = pin[:6] # 처음부터 6까지
num = pin[7:] # 7부터 끝까지
print(yyyymmdd) # 881120 출력
print(num) # 1068234 출력

# 4번 문제
pin = "881120-1068234"
print(pin[7]) # 1번 남자 2번 여자

# 5번 문제
a = "a:b:c:d"
b = a.replace(":", "#") # : -> #로 변경
print(b) # a#b#c#d

# 6번 문제
a = [1, 3, 5, 4, 2]
a.sort() # 정렬
a.reverse() # 뒤집기
print(a) # [5, 4, 3, 2, 1]

# 7번 문제
a = ['Life', 'is', 'too', 'short'] # a변수에 문자 저장
result = " ".join(a) # result값에 join 문장 합침
print(result)

# 8번 문제
a = (1, 2, 3)
a = a + (4,)
print(a) # (1, 2, 3, 4) 출력

a = (1, 2, 3)
print(id(a)) # a의 고유 주소 값 출력
a = a + (4,)
print(a)
print(id(a)) # (4,) 값이 더해 진 후 a의 고유 주소 값 출력

# 9번 문제

# a[[1]] = 'python'

# 10번 문제

a = {'A':90, 'B':80, 'C':70}
result = a.pop('B')
print(a) # {'A':90, 'C':70}출력
print(result) # 80 출력

# 11번 문제
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a) # a 리스트를 집합자료형으로 변환
b = list(aSet) # 집합자료형을 리스트 자료형으로 다시 변환
print(b) # [1,2,3,4,5] 출력

# 12번 문제
# [1, 4, 3]이 출력된다. 
# a와 b변수는 모두 동일한 [1,2,3]이라는 리스트 객체를 가리키고 있기 때문

