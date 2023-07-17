# 변수에 값 할당을 if, else로 축약하기
x = 5
if x == 10:
    y = x
else:
    y = 0

print(y)

# 위의 코드를, "변수 = 값 if 조건문 else 값" 형식으로 축약할 수 있으며,
# 이런 문법을 조건부 표현식(conditional expression)이라고 부른다.
x = 5
y = x if x == 10 else 0




# 파이썬 문법 중, False로 취급하는 것들
# - None
# - False
# - 0인 숫자들: 0, 0.0, 0j
# - 비어 있는 문자열, 리스트, 튜플, 딕셔너리, 세트: '', "", [], {}, set()
# - 클래스 인스턴스의 __bool__(), __len__() 메서드가 0 또는 False를 반환할 때