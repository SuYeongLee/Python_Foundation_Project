# 딕셔너리 자료형
dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(dic)

a = {1: 'hi'}
print(a)

a = {'a': [1,2,3]}
print(a)

# 딕셔너리 쌍 추가, 삭제하기

# 1. 딕셔너리 쌍 추가하기
a = {1: 'a'}
a[2] = 'b' #{2:'b'}쌍 추가
print(a)

a['name'] = 'pey' # {'name':'pey'} 쌍 추가
print(a)

a[3] = [1, 2, 3] # {3:[1, 2, 3]} 쌍 추가
print(a)

# 2. 딕셔너리 요소 삭제하기
del a[1] # key가 1인 key:value 쌍 삭제
print(a)

# 딕셔너리를 사용하는 방법
# 사람이름과 특기를 한 쌍으로 하는 것이 딕셔너리
# {"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "귀도":"파이썬"}

# 1. 딕셔너리에서 Key 사용해 Value 얻기
# {key값 : Value값}

grade = {'pey' : 10, 'julliet' : 99}
print(grade['pey']) # key가 'pey'인 딕셔너리의 Value를 반환
print(grade['julliet']) # key가 'julliet'인 딕셔너리의 Value를 반환

a = {1:'a', 2:'b'}
print(a[1]) # Key가 1인 요소의 Value를 반환
print(a[2]) # Key가 2인 요소의 Value를 반환

a = {'a':1, 'b':2}
print(a['a'])
print(a['b'])

dic = {'name':'pey','phone':'0119993323', 'birth':'1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

