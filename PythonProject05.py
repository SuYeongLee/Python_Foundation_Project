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

# 2. 딕셔너리 만들 때 주의할 사항

a = {1:'a', 1:'b'} # 1이라는 Key 값이 증복으로 사용
print(a) # 1:'a' 쌍이 무시됨

# 리스트로 Key를 설정하면?

# a = {[1,2] : 'hi'} # 리스트를 key로 사용
# print(a) # Key값은 딕셔너리로 사용 할 수 없음

# 딕셔너리 관련 함수

# 1. Key 리스트 만들기(keys)

a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys()) # 딕셔너리 a의 Key만을 모아서 dict_keys 객체를 돌려줌

for k in a.keys():
    print(k)

print(list(a.keys())) # dict_keys 객체를 리스트로 변환

# 2. Value 리스트 만들기(values)
print(a.values())

# 3. key, Value 쌍 얻기(items)
print(a.items())

# 4. key:Value 쌍 모두 지우기(clear)
a.clear()
print(a)

# 5. key로 value 얻기(get)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))
print(a.get('birth'))


a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.get('nokey')) # None을 리턴함
# print(a['nokey'])

print(a.get('foo', 'bar'))

# 6. 해당 key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey','phone':'0119993323','birth':'1118'}
print('name' in a) # 딕셔너리 안에 존재하므로 True
print('email' in a) # 딕셔너리 안에 존재하지 않으므로 False

# 연습문제
dic = {'name':'홍길동','birth':'1128','age':'30'}
print(dic)