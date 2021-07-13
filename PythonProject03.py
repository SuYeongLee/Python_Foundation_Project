# 리스트 자료형

# 리스트는 어떻게 만들고 사용할까?
odd = [1, 3, 5, 7, 9]
print(odd)

# 리스트명 = [요소1, 요소2, 요소3, ...]

a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, 'Life', 'is']
e = [1, 2, ['Life', 'is']]

print(a)
print(b)
print(c)
print(d)
print(e)

# 리스트의 인덱싱과 슬라이싱

# 1. 리스트의 인덱싱
a = [1, 2, 3]
print(a)
print(a[0])
print(a[0] + a[2]) # 1 + 3
print(a[-1])

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])
print(a[-1])
print(a[3])

print(a[-1][0])
print(a[-1][1])
print(a[-1][2])

# 삼중 리스트에서 인덱싱하기
a = [1, 2, ['a', 'b', ['Life', 'is']]]

print(a[2][2][0])


# 2. 리스트의 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[0:2])

a = "12345"
print(a[0:2])

a = [1, 2, 3, 4, 5]
b = a[:2] # 처음부터 a[1]까지
c = a[2:] # a[2]부터 마지막까지
print(b)
print(c)


# 연습문제
A = [1, 2, 3, 4, 5]
print(A[1:3])

# 중첩된 리스트에서 슬라이싱하기
a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5]) # a[2]부터 a[4]까지
print(a[3][:2])

# 리스트 연산하기

# 1. 리스트 더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# 2. 리스트 반복하기(*)
a = [1, 2, 3]
print(a * 3)

# 3. 리스트 길이 구하기
a = [1, 2, 3]
print(len(a))

# 초보자가 실수하기 쉬운 리스트 연산 오류
a = [1, 2, 3]
# a[2] + "hi" # 정수와 문자열은 서로 더할 수 없음
str(a[2]) + "hi" # str함수는 정수나 실수를 문자열의 형태로 바꾸어 주는 파이썬 내장 함수

# 리스트의 수정과 삭제
# 1. 리스트에서 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)

# 2. del함수 사용해 리스트 요소 삭제하기
a = [1, 2, 3]
del a[1]
print(a)

# del 함수로 여러개 삭제
a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

# 리스트 관련 함수
# 1. 리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4) # 리스트의 맨 마지막에 4를 추가
print(a)

a.append([5,6]) # 리스트의 맨 마지막에 [5,6]을 추가
print(a)

# 2. 리스트 정렬(sort)
# sort 함수는 리스트의 요소를 순서대로 정렬해 준다.

a = [1, 4, 3, 2]
a.sort()
print(a)

a = ['a','c','b']
a.sort()
print(a)

# 3. 리스트 뒤집기(reverse)
a = ['a','c','b']
a.reverse()
print(a)

# 4. 위치 반환(index)
a = [1, 2, 3]
print(a.index(3)) # 3은 리스트 a의 세 번째(a[2]) 요소
print(a.index(1)) # 1은 리스트 a의 첫번째(a[0]) 요소

# 5. 리스트에 요소 삽입(insert)
a = [1, 2, 3]
a.insert(0, 4) # a[0] 위치에 4 삽입
print(a)

a.insert(3, 5) # a[3] 위치에 5 삽입
print(a)

# 6. 리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

a.remove(3)
print(a)

# 7. 리스트 요소 끄집어내기(pop)
a = [1, 2, 3]
print(a.pop())
print(a)

a = [1, 2, 3]
print(a.pop(1))
print(a)