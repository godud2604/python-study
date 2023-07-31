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

b_1 = [i + 5 for i in range(10) if i % 2 == 1]




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
    


# 22.6 리스트에 map 사용하기
"""
- list(map(함수, 리스트))
- tuple(map(함수, 튜플))
"""
a = [1.2, 2.5, 3.7, 4.6]
for i in range(len(a)):
    a[i] = int(a[i])

print(a)


b = list(map(int, a))
print(b)


# c = map(int, input().split()) 
# list(c) # [10, 20]




# 22.7 튜플 응용하기
"""
- 튜플은 리스트와는 달리 내용을 변경할 수 없다 => 불변(immutable)
- 따라서, 내용을 변경하는 append 같은 메서드는 사용할 수 없고, 요소의 정보를 구하는 메서드만 사용할 수 있다.
"""



# 22.7.4 튜플 표현식 사용하기
"""
- 튜플을 리스트 표현식처럼 생성할 때는, tuple 안에 for 반복문과 if 조건문을 지정
- tuple(식 for 변수 in 리스트 if 조건식)

- 참고로, ()(괄호) 안에 표현식을 넣으면 튜플이 아니라 제너레이터 표현식이 된다.
"""

a = tuple(i for i in range(10) if i % 2 == 0)
print('tuple a', a) # (0, 2, 4, 6, 8)

b = (i for i in range(10) if i % 2 == 0)
print('제너레이터 b', b) # <generator object <genexpr> at 0x10b01e740>

