# random 모듈을 사용해서 재밌는 함수 만들기
import random

# 방법 1
# def random_pop(data):
#     number = random.randint(0, len(data)-1)
#     return data.pop(number)

# 방법 2
# def random_pop(data):
#     number = random.choice(data)
#     data.remove(number)
#     return number


# if __name__ == "__main__":
#     data = [1,2,3,4,5]
#     while data: print(random_pop(data))

import random
data = [1, 2, 3, 4, 5]
random.shuffle(data)
print(data)