# 사용자 입력과 출력

# input의 사용
# a = input() # 사용자가 입력한 문장을 a에 대입
# 입력 : Life is too short, you need ptyhon

#print(a)

# ※ 프롬프트 값을 띄어서 사용자 입력받기

# number = input("숫자를 입력하세요: ")
# print(number)

# print 자세히 알기

a = 123
print(a) # 숫자 출력하기

a = "Python"
print(a) # 문자열 출력하기

a = [1, 2, 3]
print(a) # 리스트 출력하기

# 1. 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일하다
print("life" "is" "too short") # 1
print("life" + "is" + "too short") # 2

# 2. 문자열 띄어쓰기는 콤마로 한다
print("Life", "is", "too short")

# 3. 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=' ')
