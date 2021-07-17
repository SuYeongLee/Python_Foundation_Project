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