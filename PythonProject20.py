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
# time.time
# import time
# print(time.time())

# time.localtime
# print(time.localtime(time.time()))

# time.asctime
# print(time.asctime(time.localtime(time.time())))

# time.ctime
# print(time.ctime())

# time.strftime
# print(time.strftime('출력할 형식 포맷 코드', time.localtime(time.time())))

# import time
# print(time.strftime('%x', time.localtime(time.time())))
# print(time.strftime('%c', time.localtime(time.time())))

# time.sleep
# sleep1.py 참고

# calendar
# calendar.calendar(연도) - 그해의 전체 달력을 볼 수 있음

import calendar
print(calendar.calendar(2021))

# calendar.prcal(연도) - 위와 같은 결과값
calendar.prcal(2021)

# 2021년 12월 달력만 불러옴
calendar.prmonth(2021, 12)

# calendar.weekday
print(calendar.weekday(2021, 12, 31))

# calendar.monthrange
print(calendar.monthrange(2021,12))