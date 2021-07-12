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

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[2:5]) # a[2]부터 a[4]까지
print(a[3][:2])