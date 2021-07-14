# 불 자료형

a = True
b = False

print(type(a))
print(type(b))

print(1 == 1)
print(2 > 1)
print(2 < 1)

# 자료형의 참과 거짓

# while 조건문:
#   수행할 문장

a = [1, 2, 3, 4]
while a: # a가 참인 동안 
    print(a.pop()) # 리스트의 마지막 요소를 하나씩 꺼낸다.

# []비어 있는 리스트이므로 거짓
if []: # 만약 []가 참이면
    print("참") # '참' 문자열 출력
else: # 만약[]가 거짓이면
    print("거짓") # '거짓' 문자열 출력

# [1, 2, 3]에 들어 있을 경우 참
if [1, 2, 3]: # 만약 []가 참이면
    print("참") # '참' 문자열 출력
else: # 만약[]가 거짓이면
    print("거짓") # '거짓' 문자열 출력

# 불 연산

print(bool('python'))
print(bool(''))

print(bool([1,2,3]))
print(bool([]))

print(bool(0))
print(bool(3))