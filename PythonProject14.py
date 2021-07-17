# 파일 읽고 쓰기

# r : 읽기 모드 - 파일을 읽기만 할 때 사용
# w : 쓰기 모드 - 파일에 내용을 쓸 때 사용
# a : 추가 모드 - 파일의 마지막에 새로운 내요을 추가할 때 사용

# 1. 파일 생성하기
# 파일 객체 = open(파일 이름, 파일 열기 모드)

# (1)
# f = open("PythonProject14연습.txt",'w')
# f.close()

# (2)
# f = open("C:/CodeProject/Python_Foundation_Project/PythonProject14연습.txt", 'w')
# f.close()

# 2. 파일을 쓰기 모드로 열어 출력값 적기
# f = open("PythonProject14연습.txt",'w')
# for i in range(1, 11): # 1부터 10까지 i에 대입
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data) # data를 파일 객체 f에 써라
# f.close()

# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     print(data)

# 프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법

# 1. readline 함수 사용하기

# f = open("C:/CodeProject/Python_Foundation_Project/PythonProject14연습.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

# 파일을 사용한 입력 방법

# f = open("C:/CodeProject/Python_Foundation_Project/PythonProject14연습.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# 키보드를 사용한 입력방법

# while 1:
#     data = input()
#     if not data: break
#     print(data)

# 2. readlines 함수 사용하기
# f = open("C:/CodeProject/Python_Foundation_Project/PythonProject14연습.txt", 'r')
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

# 3. read 함수 사용하기
# f = open("C:/CodeProject/Python_Foundation_Project/PythonProject14연습.txt", 'r')
# data = f.read()
# print(data)
# f.close()

# 파일에 새로운 내용 추가하기
# f = open("C:/CodeProject/Python_Foundation_Project/PythonProject14연습.txt", 'a')
# for i in range(11, 20): # 11부터 19까지 i에 대입
#     data = "%d 번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# with문과 함께 사용하기

# f = open("foo.txt", 'w')
# f.write("Life is too short, you need python")
# f.close()

# with open("foo.txt", "w") as f:
#     f.write("Life is too short, you need python")

# sys 모듈로 매개변수 주기

# 명령 프롬프트 명령어 [인수1 인수2]

# import sys

# args = sys.argv[1:]
# for i in args:
#     print(i)

# import sys
# args = sys.argv[1:]
# for i in args:
#     print(i.upper(), end=' ')