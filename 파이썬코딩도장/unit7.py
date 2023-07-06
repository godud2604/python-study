# sep로 값 사이에 문자 넣기
print("Hello", "Python", sep = " ")

# 줄바꿈 활용하기
print(1, 2, 3, sep='\n')

# end에 빈 문자열을 지정하면 다음번 출력이 바로 뒤에 오게 됨
print(1, end=" ")
print(2, end=" ")
print(3)

"""
숫자를 콤마로 구분해서 표현 ?
- 보통 가격이나 큰 숫자를 10,000,000으로 표현해야 할 때 파이썬은 _(밑줄 문자)를 사용한다.
- 만약 숫자에 ,를 사용하면 파이썬의 튜플 자료형이 되므로 주의.
"""
print(10000000)
print(10_000_000)
print(10,000,000)


"""
sys.getrefcount
- 현재 객체가 몇 번 사용되었는지 확인할 수 있다. (객체를 사용(참조)한 횟수를 레퍼런트 카운트)
"""
import sys
print(sys.getrefcount(1000))

x = 1000
print(sys.getrefcount(1000))

y = 1000
print(sys.getrefcount(1000))

# 객체가 같은지 판단하는 연산자 => is
print(x is y) 

