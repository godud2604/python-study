# 25.1.1 딕셔너리에 키-값 쌍 추가하기
"""
- setdefault : 키-값 쌍 추가
- update : 키의 값 수정, 키가 없으면 키-값 쌍 추가

=> setdefault와 update의 차이
- setdefault : 키-값 쌍 추가만 할 수 있고, 이미 들어있는 키의 값은 수정할 수 없다.
- update : 키-값 쌍 추가와 값 수정이 모두 가능하다. 
"""

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
print(x) # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None}

x.update(a=90, e=50, f=60)
print(x) # {'a': 90, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}

# update(반복가능한객체) : 키-값 쌍으로 된 반복 가능한 객체로 값을 수정한다.
y = {1: 'one', 2: 'two'}
y.update(zip([1, 2, 3], ['one', 'two', 'three']))
print(y) # {1: 'one', 2: 'two', 3: 'three'}



# 25.1.4 딕셔너리에서 키-값 쌍 삭제하기
"""
- pop(키) : 딕셔너리에서 특정 키-값 쌍을 삭제한 뒤 삭제한 값을 반환한다.
- pop(키, 기본값)
  : 기본값 지정 시, 딕셔너리에 키가 있을 때는 해당 키-값 쌍을 삭제한 뒤 삭제한 값을 반환하지만,
    키가 없을 때는 기본값만 반환한다.
"""
z = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(z.pop('a')) # 10

print(z.pop('z', 'default value...')) # default value...



# 25.3 딕셔너리 표현식 사용하기
"""
- {키: 값 for 키, 값 in 딕셔너리}
- dict({키: 값 for 키, 값 in 딕셔너리})
"""
keys = ['a', 'b', 'c', 'd']

x = {key: value for key, value in dict.fromkeys(keys).items()}
print(x) # {'a': None, 'b': None, 'c': None, 'd': None}

