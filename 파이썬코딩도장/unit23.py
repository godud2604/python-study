# 23.3.3 리스트 표현식으로 2차원 리스트 만들기

a = [[0 for j in range(2)] for i in range(3)]

b = [[0] * 2 for i in range(3)]
# print([0] * 2) [0, 0]



# 23.3.4 톱니형 리스트 만들기
c = [[0] * i for i in [3, 1, 3, 2, 5]]
print(c)



# sorted로 2차원 리스트 정렬하기
"""
- sorted(반복가능한객체, key=정렬함수, reverse=True 또는 False)
"""
students = [
    ["john", "C", 19],
    ["maria", "A", 25],
    ["andrew", "B", 7],
]

d = sorted(students, key = lambda student: student[1]) # 안쪽 리스트의 인덱스 1을 기준으로 정렬
print(d)



"""
2차원 이상의 다차원 리스트는 리스트를 완전히 복사하려면 copy 메서드 대신, deepcopy 함수를 사용해야 한다.
"""
import copy

a = [[10, 20], [30, 40]]
b = copy.deepcopy(a) # copy.deepcopy 함수를 사용하여 깊은 복사
b[0][0] = 500

print(a) # [[10, 20], [30, 40]]
print(b) # [[500, 20], [30, 40]]