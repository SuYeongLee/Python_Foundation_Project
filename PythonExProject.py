# 연습문제함

# 112 ~ 115P
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

# 146P ~ 148P

# 1번 문제

# 첫 번째 조건 : "wife"라는 단어는 a문자열에 없으므로 거짓이다.
# 두 번째 조건 : "python"이라는 단어는 a 문자열에 있지만 "you" 역시 a 문자열에 있으므로 거짓이다.
# 셋 번째 조건 : "shirt"라는 단어가 a 문자열에 없으므로 참이다.
# 네 번재 조건 : "need"라는 단어가 a 문자열에 있으므로 참이다.

# 가장 먼저 참이 되는 것이 세 번째 조건이므로 "shirt"가 출력된다.

# 2번 문제

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0: # 3으로 나누어 떨어지는 수는 3의 배수
        result += i
    i += 1

print(result) # 166833 출력

# 3번 문제
i = 0
while True:
    i += 1 # while문 수행 시 1씩 증가
    if i > 5: break # i 값이 5보다 크면 while문을 벗어난다.
    print('*' * i) # i 값 개수만큼 *를 출력한다.

# 4번 문제
for i in range(1, 101):
    print(i)

# 5번 문제
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score # A학급의 정수를 모두 더한다.
average = total / len(A) # 평균을 구하기 위해 총 점수를 총 학생수로 나눈다.
print(average) # 평균 79.0이 출력된다.

# 6번 문제
numbers = [1, 2, 3, 4, 5]

result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n %2 == 1]
print(result)

if 'card' not in pocket:
    print("걸어 가라")
else:
    print("버스를 타고 가라")

a = 0
while a < 10:
    a = a + 1
    if a % 3 == 0: continue
    print(a)

a = 0
for i in range(1, 101):
    a += i

print(a)