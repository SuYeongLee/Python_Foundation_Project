# while문

#while 조건문:
#   수행할 문장1
#   수행할 문장2
#   수행할 문장3

treeHit = 0 # 나무를 찍은 횟수
while treeHit < 10: #나무를 찍은 횟수가 10보다 작은 동안 반복
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10: #나무를 열 번 찍으면
        print("나무 넘어갑니다.")

#while문 만들기

#prompt = ""
#1.Add
#2.Del
#3.List
#4.Quit

# Enter number: ""

# number = 0 # 번호를 입력받을 변수
# while number != 4: # 입력받은 번호가 4가 아닌 동안 반복한다.
#     print(prompt)
#     number = int(input())
# #1.Add
# #2.Del
# #3.List
# #4.Quit

# Enter number: