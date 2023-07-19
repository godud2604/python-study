# 리스트 조작하기
"""
# 리스트에 요소 추가하기
- append : 요소 하나를 추가
- extend : 리스트를 연결하여 확장
- insert : 특정 인덱스에 요소 추가

# 리스트에서 요소 삭제하기
- pop : 마지막 요소 또는 특정 인덱스의 요소를 삭제
- remove : 특정 값을 찾아서 삭제
"""



# 리스트로 큐 만들기
from collections import deque

a = deque([10, 20, 30])
a.append(500)
print(a)

a.popleft() # 덱의 왼쪽 요소를 삭제
print(a)

a.appendleft(100) # 덱의 왼쪽에 요소를 추가
print(a)




# 리스트의 할당과 복사 알아보기
a = [0, 0, 0, 0, 0]
b = a
print(a is b) # True

c = a.copy()
print(a is c) # False
print(a == c) # True (복사된 요소는 같으므로)




# 가장 작은 수와 가장 큰 수 구하기
a = [38, 21, 53, 62, 19]
smallest = a[0]

for i in a:
    if i < smallest:
        smallest = i

print('smallest', smallest)




# 리스트 표현식 사용하기
"""
리스트 안에 식, for 반복문, if 조건문 등을 지정하여 리스트를 생성하는 것을 리스트 컴프리헨션(list comprehension)이라고 한다.
=> 즉, 식으로 지정해서 생성된 것을 리스트로 잡아두는 것이 리스트 컴프리헨션
=> 간단하게 리스트 표현식이라고 사용한다.

- [식 for 변수 in 리스트]
- list(식 for 변수 in 리스트)
"""
a = [i for i in range(10)] # 0부터 9까지 숫자를 생성하여 리스트 생성
b = list(i for i in range(10))


c = [i + 5 for i in range(10)] # 0부터 9까지 숫자를 생성하면서 값에 5를 더하여 리스트 생성
d = [i* 2 for i in range(10)]





# 리스트 표현식에서 if 조건문 사용하기
"""
- [식 for 변수 in 리스트 if 조건식]
- list(식 for 변수 in 리스트 if 조건식)
"""
a = [i for i in range(10) if i % 2 == 0] # 0~9 숫자 중 2의 배수만 숫자

b = [i + 5 for i in range(10) if i % 2 == 1]





# 22.5.2 for 반복문과 if 조건문을 여러 번 사용하기
"""
[식 for 변수1 in 리스트1 if 조건식1
    for 변수2 in 리스트2 if 조건식2
    ...
    for 변수n in 리스트n if 조건식n]
"""
a = [i * j for j in range(2, 10) for i in range(1, 10)]

for j in range(2, 10):
    for i in range(1, 10):
        print(i * j)
    