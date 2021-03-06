# 스레드를 다루는 threading 모듈
# import time

# def long_task():
#     for i in range(5):
#         time.sleep(1) # 1초간 대기
#         print("working:%s\n" % i)

# print("Start")

# for i in range(5):  # long_task를 5회 수행한다.
#     long_task()

# print("End")

# import time
# import threading # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.

# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print("working:%s\n" % i)
# print("Start")

# threads = []
# for i in range(5):
#     t = threading.Thread(target=long_task) # 스레드를 생성한다.
#     threads.append(t)

# for t in threads:
#     t.start() # 스레드를 실행한다.

# print("End")

import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)
for t in threads:
    t.start()
for t in threads:
    t.join() # join으로 스레드가 종료될 때까지 기다린다.

print("End")