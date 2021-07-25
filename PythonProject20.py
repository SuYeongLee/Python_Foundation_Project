# 라이브러리

# sys
# argv_test.py 참고 

# import sys
# sys.path

# path_append.py

# pickle
# import pickle
# f = open("test.txt", 'wb')
# data = {1: 'python', 2: 'you need'}
# pickle.dump(data, f)
# f.close()

# import pickle
# f = open("test.txt", 'rb')
# data = pickle.load(f)
# print(data)

# OS
# 내 시스템의 환경 변수 값을 알고 싶을 때 - os.environ

# import os
# os.environ

# os.environ['PATH']

# 디렉터리 위치 변경하기 - os.chdir

# os.chdir("C:/WINDOWS")

# 디렉터리 위치 돌려받기 - os.getcwd

# print(os.getcwd())

# 시스템 명령어 호출하기 - os.system
# os.system("dir")

# 실행한 시스템 명령어의 결괏값 돌려받기 - os.popen
# f = os.popen("dir")

# print(f.read())

# 기타 유용한 os 관련 함수
#  os.mkdir(디렉터리) : 디렉터리를 생성한다.
#  os.rmdir(디렉터리) : 디렉터리를 삭제한다. (단 디렉터리가 비어 있어야 삭제가 가능하다.)
#  os.unlink(파일 이름) : 파일을 지운다.
#  os.rename(src, dst) : src라는 이름의 파일을 st라는 이름으로 바꾼다.

# shutil

# import shutil
# shutil.copy("src.txt", "dst.txt")

# glob

# 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)

# import glob
# glob.glob("C:/CodeProject/Python_Foundation_Project*")

# tempfile
# import tempfile
# filename = tempfile.mkstemp()
# print(filename)

# import tempfile
# f = tempfile.TemporaryFile()
# f.close() # 생성한 임시 파일이 자동으로 삭제됨

# time
# 시간과 관련된 time 모듈에는 함수가 굉장히 많다. 그중 가장 유용한 몇 가지만 알아보자.

# time.time
# utc를 사용하여 현재 시간을 실수 형태로 돌려주는 함수

# import time
# print(time.time())

# time.localtime
# 돌려준 실수 값을 사용해서 
# 연도, 월,일,시,분,초,...의 형태로 바꾸어 주는 함수
# print(time.localtime(time.time()))

# time.asctime
# 반환된 튜플 형태의 값을 인수로 받아서 날짜와 
# 시간을 알아보기 쉬운 형태로 돌려주는 함수
# print(time.asctime(time.localtime(time.time())))

# time.ctime
# 현재 시간만을 돌려준다.
# print(time.ctime())

# time.strftime
# 시간에 관계된 것을 세밀하게 표현
# print(time.strftime('출력할 형식 포맷 코드', time.localtime(time.time())))

# import time
# print(time.strftime('%x', time.localtime(time.time())))
# print(time.strftime('%c', time.localtime(time.time())))

# time.sleep
# 일정한 시간 가격을 두고 루프를 실행 할 수 있다.
# sleep1.py 참고

# calendar
# 파이썬에서 달력을 볼 수 있게 해주는 모듈

# calendar.calendar(연도) - 그해의 전체 달력을 볼 수 있음

# import calendar
# print(calendar.calendar(2021))

# calendar.prcal(연도) - 위와 같은 결과값
# calendar.prcal(2021)

# 2021년 12월 달력만 불러옴
# calendar.prmonth(2021, 12)

# calendar.weekday
# print(calendar.weekday(2021, 12, 31))

# calendar.monthrange
# print(calendar.monthrange(2021,12))

# random
# 난수를 발생시키는 모듈

# import random
# print(random.random())
# print(random.randint(1, 10))
# print(random.randint(1, 55))

# random_pop.py참고

# webbrowser
# 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈
import webbrowser
webbrowser.open("http://google.com")