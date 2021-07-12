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
print("<문자열 슬라이싱>")
print(a[0:4])
print(a[0:3])
print(a[0:5])
print(a[0:2])
print(a[5:7])
print(a[12:17])
print(a[19:])
print(a[:17])
print(a[:])
print(a[19:-7])

# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)

a = "20010331Rainy"
year = a[:4] # 처음부터 a[3]까지
day = a[4:8] # a[4]부터 a[7]까지
weather = a[8:] # a[8]부터 마지막까지
print(year)
print(day)
print(weather)


# Pithon이라는 문자열을 Python으로 바꾸려면?
a = "Pithon"
print(a[:1])
print(a[2:])
print(a[:1] + 'y' + a[2:])

# 문자열 포매팅

# 1. 숫자 바로 대입
print("I eat %d apples."%3)

# 2. 문자열 바로 대입
print("I eat %s apples." % "five")

# 3. 숫자 값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)

# 4. 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

# 문자열 포맷 코드
# %s : 문자열(String)
# %c : 문자 1개(Character)
# %d : 정수(Integer)
# %f : 부동 소수(Floating-point)
# %o : 8진수
# %x : 16진수
# % % : Literal % (문자 '%' 자체)

# 연습문제
print("I have %s apples" %3)
print("rate is %s"% 3.234)
print("Error is %d%%." % 98)

# 포맷 코드와 숫자 함께 사용하기
# 1. 정렬과 공백

print("%10s" % "hi") # 오른쪽 정렬
print("%-10sjane" % 'hi') # 왼쪽 정렬

# 2. 소수점 표현하기
print("%0.4f" %3.42134234) # 소수점 네 번째 자리까지만 나타내고 싶은 경우
print("%10.4f" % 3.42134234) # 소수점 네 번째 자리까지만 표시 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬

# format함수를 사용한 포매팅

# 1. 숫자 바로 대입하기
print("I eat {0} apples".format(3))

# 2. 문자열 바로 대입하기
print("I eat {0} apples".format("five"))

# 3. 숫자 값을 가진 변수로 대입하기
number = 3
print("I eat {0} apples".format(number))

# (1) 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days.".format(number, day))

# (2) 이름으로 넣기
print("I ate {number} apples. so Iwas sick for {day} days.".format(number = 10, day = 3))

# (3) 인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick for {day} days.".format(10, day = 3))

# (4) 왼쪽 정렬
print("{0:<10}".format("hi"))

# (5) 오른쪽 정렬
print("{0:>10}".format("hi"))

# (6) 가운데 정렬
print("{0:^10}".format("hi"))

# (7) 공백 채우기
print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))

# (8) 소수점 표현하기
y = 3.42134234

# {값:자리수.소수점 자리수}
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))

# (9) { 또는 } 문자 표현하기
print("{{ and }}".format())

# (10) f 문자열 포매팅
name = "이수영"
age = '28'
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

age = 30
print(f'나는 내년이면 {age+1}살이 된다.')

# 딕셔너리 f문자열 포매팅
d = {'name': '이수영', 'age':27}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

# f문자열 포매팅 정렬
print(f'{"hi":<10}') # 왼쪽 정렬
print(f'{"hi":>10}') # 오른쪽 정렬
print(f'{"hi":^10}') # 가운데 정렬

# f문자열 포매팅 공백채우기
print(f'{"hi":=^10}') # 가운데 정렬하고 = 문자로 공백 채우기
print(f'{"hi":!<10}') # 왼쪽 정렬하고 ! 문자로 공백 채우기

# f문자열 포매팅 소수점
y = 3.42134234
print(f'{y:0.4f}') # 소수점 4자리까지만 표현
print(f'{y:10.4f}') # 소수점 4자리까지 표현하고 총 자리숫를 10으로 맞춤

# f문자열 문자표현
print(f'{{ and }}')

# 연습문제
print(f'{"python":!^12}') # f문자열 방식
print('{0:!^12}'.format("python")) # format 방식


# 문자열 관련 함수
# 1. 문자 개수 세기(count)
a = "hobby"
print(a.count('b'))

# 2. 위치알려주기 1(find)
a = "Python is the best choice"
print(a.find('b'))
print(a.find('k')) # 문자에 없을 경우 -1로 반환

# 3. 위치 알려주기 2(index)
a = "Life is too short"
print(a.index('t'))

# 4. 문자열 삽입(join)
print(",".join('abcd'))
print(",".join(['a','b','c','d']))

# 5. 소문자를 대문자로 바꾸기(upper)
a = "hi"
print(a.upper())

# 6.대문자를 소문자로 바꾸기(lower)
a = "HI"
print(a.lower())

# 7. 왼쪽 공백 지우기(lstrip)
a = " hi "
print(a.lstrip())

# 8. 오른쪽 공백 지우기(rstrip)
a = " hi "
print(a.rstrip())

# 9. 양쪽 공백 지우기(strip)
a = " hi "
print(a.strip())

# 10. 문자열 바꾸기(replace)
a = "Life is too short"
# (바뀌게 될 문자열, 바꿀 문자열)
print(a.replace("Life", "Your leg"))

# 11. 문자열나누기(split)
a = "Life is too short"
print(a.split()) # 공백을 기준으로 문자열 나눔
b = "a:b:c:d"
print(b.split(':')) # : 기호를 기준으로 문자열 나눔
