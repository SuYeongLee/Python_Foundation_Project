# 예외 처리

# try : 오류가 발생할 수 있는 구문
# ecept Exception as e : 오류 발생
# else : 오류 발생하지 않음
# finally : 무조건 마지막에 실행


# 없는 파일을 열려고 할때
# f = open("나없는파일", 'r')


# try:
#     4/0
# except ZeroDivisionError as e:
#     print(e)

# print("안녕하세요")


# try:
#     f = open('none', 'r')
# except FileNotFoundError as e:
#     print(str(e))
# else:
#     data = f.read()
#     print(data)
#     f.close()

# f = open('foo.txt', 'w')
# try:
#     # 무언가를 수행한다.
#     data = f.read()
#     print(data)
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError:
#     print("0으로 나눌 수 없습니다.")
# except IndexError:
#     print("인덱싱할 수 없습니다.")


# 여러 개의 오류 처리하기

# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except ZeroDivisionError as e:
#     print(e)
# except IndexError as e:
#     print(e)

# try:
#     a = [1,2]
#     print(a[3])
#     4/0
# except (ZeroDivisionError, IndexError) as e:
#     print(e)

# 오류 회피하기

# try:
#     f = open("나없는파일", "r")
# except FileNotFoundError: # 파일이 없더라도 오류를 발생시키지 않고 통과한다.
#     pass

# 오류 일부러 발생시키기

# class Bird:
#     def fly(self):
#         raise NotImplementedError

# class Eagle(Bird): #Eagle 클래스는 Bird 클래스를상속 받음
#     pass

# eagle = Eagle()
# eagle.fly()

# class Eagle(Bird):
#     def fly(self):
#         print("very fast")

# eagle = Eagle()
# eagle.fly()

# 예외 만들기

# class MyError(Exception):
#     pass

# def say_nick(nick):
#     if nick == '바보':
#         raise MyError()
#     print(nick)

# say_nick("천사")
# say_nick("바보")

# try:
#     say_nick("천사")
#     say_nick("바보")
# except MyError:
#     print("허용되지 않는 별명입니다.")

# try:
#     say_nick("천사")
#     say_nick("바보")
# except MyError as e:
#     print(e)

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."