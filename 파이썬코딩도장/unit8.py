# id 함수 
print(id(1)) # 4368005424
print(id(1.0)) # 4369420528



# is
a = -5
print(a is -5)
a = -6
print(a is -6)



# 정수, 실수, 문자열을 불로 만들기
print(bool(1))
print(bool(0))
print(bool(1.5))
print(bool('False'))



# 단락평가
# => 논리 연산자는 마지막으로 단락 평가를 실시한 값을 그대로 반환
# => 논리 연산자는 무조건 불을 반환하지 않는다.
print(True and 'Python') # Python
print('Python' and True) # True
print('Python' and False) # False

# or 연산자도 마찬가지로, 마지막으로 단락 평가를 실시한 값이 반환된다.
# => 밑의 예제는 or 연산자에서 첫 번째 값만으로 결과가 결정되므로 첫 번째 값이 반환된다.
print(True or 'Python') # True