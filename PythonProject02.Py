#문자열 자료형

# ※ 문자열 사용법

# 1. 큰따옴표(")로 양쪽 둘러싸기
print("Hello World")

# 2. 작은따옴표(')로 양쪽 둘러싸기
print('Python is fun')

# 3. 큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
print("""Life is too short, You need python""")

# 4. 작은따옴표 3개 연속(''')으로 써서 양쪽 둘러싸기
print('''Life is too short, You need python''')


# ※ 문자열 안에 작은따옴표나 큰 따옴표를 포함시킬때

# 1. 문자열에 작은따옴표(') 포함시키기
food = "Python's favorite food is perl"
print(food)
food = "Python's favorite food is perl"

# 2. 문자열에 큰따옴표(") 포함시키기
say = '"Python is very easy." he says.'
print(say)

# 3. 백슬래시(\)를 사용해서 작은따옴표(')와 큰따옴표(")를 문자열에 포함시키기
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

print(food)
print(say)

# ※ 여러 줄인 문자열을 변수에 대입

# 1. 줄을 바꾸는 이스케이프 코드'\n' 삽입하기
multiline = "Life is too short\nYou need python"
print(multiline)

# 2. 연속된 작은따옴표 3개(''')Ehsms zmsEkdhavy 3ro(""")사용하기
multiline = '''
Life is too short
You need python
'''
print(multiline)

multiline = """
Life is too short
You need python
"""

print(multiline)

# \n : 문자열 안에서 줄을 바꿀 때 사용
# \t : 문자열 사이에 탭 간격을 줄 때 사용
# \\ : 문자 \를 그대로 표현할 때 사용
# \' : 작은따옴표(')를 그대로 표현할 때 사용
# \" : 큰따옴표(")를 그대로 표현할 때 사용
# \r : 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
# \f : 폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
# \a : 벨 소리(출력할 때 PC 스피커에서 '삑'소리가 난다.)
# \b : 백스페이스
# \000 : 널 문자

# ※ 문자열 연산하기

# 1. 문자열 더해서 연결하기(Concatenation)
head = "Python"
tail = " is fun!"
print(head + tail)

# 2. 문자열 곱하기
a = "python"
print(a * 2) 

# 3. 문자열곱하기 응용
#multistring.py

print("=" * 50)
print("My program")
print("=" * 50)

# 4. 문자열 길이 구하기
a = "Life is too short"
print(len(a))

# 연습문제
ex = 'You need python'
print(len(ex))

# ※ 문자열 인덱싱과 슬라이싱
a = "Life is too short, You need Python"
print(a[3])

# ※ 문자열 인덱싱 활용하기
a = "Life is too short, You need Python"
print(a[0])
print(a[12])
print(a[-1])
print(a[-0])
print(a[-2])
print(a[-5])

# 문자열 슬라이싱 활용
a = "Life is too short, You need Python"
b = a[0] + a[1] + a[2] + a[3]
print(b)

a = "Life is too short, You need Python"

# a[시작 번호 : 끝 번호]
print(a[0:4])