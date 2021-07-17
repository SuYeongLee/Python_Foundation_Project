# for문

# for문의 기본 구조

# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2

# 1. 전형적인 for문 

# test_list = ['one', 'two', 'three']
# for i in test_list: # one, two, three를 순서대로 i에 대입
#     print(i)


# 2. 다양한 for문의 사용
# (first, last)
# a = [(1, 2), (3, 4), (5, 6)]
# for (first, last) in a:
#     print(first + last)

# 3. for문의 응용

# marks = [90, 25, 67, 45, 80] # 학생들의 시험 점수 리스트
# number = 0 # 학생에게 붙여 줄 번호
# for mark in marks: # 90, 25, 67, 45, 80을 순서대로 mark에 대입
#     number = number + 1
#     if mark >= 60:
#         print("%d번 학생 축하합니다. 합격입니다." % number)
#     else:
#         print("%d번 학생은 불합격입니다." % number)

# for문과 continue문
# marks2.py

# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks:
#     number = number + 1
#     if mark < 60: continue
#     print("%d번 학생 축하합니다. 합격입니다. " % number)


# for문과 함께 자주 사용하는 range 함수
# range(시작 숫자, 끝 숫자)
a = range(10)
print(a)

a = range(1, 11)
print(a)

# range 함수의 예시 살펴보기
add = 0
for i in range(1, 11):
    add = add + i
print(add)

# marks3.py
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue # 점수가 60점 미만이면 맨 처음으로 돌아간다.
    print("%d번 학생 축하합니다. 합격입니다." % (number + 1))


# for와 range를 사용한 구구단
for i in range(2, 10): # 1번 for문
    for j in range(1, 10): #2번 for문
        print(i*j, end=" ")
    print('')

# 리스트 내포 사용하기

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

# [표현식 for 항목 in 반복 가능 객체 if 조건]
# [표현식 for 항목1 in 반복 가능 객체1 if 조건1
#         for 항목2 in 반복 가능 객체2 if 조건2
#         for 항목n in 반복 가능 객체n if 조건n]

result = [x*y for x in range(2, 10)
    for y in range(1, 10)]
print(result)

