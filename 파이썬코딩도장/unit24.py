# 24.1.2 문자 바꾸기
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table)) # 1ppl2



# 24.1.4 구분자 문자열과 문자열 리스트 연결하기
list = ['apple', 'pear', 'grape']
print(' '.join(list)) # apple pear grape



# 24.2.1 서식 지정자로 문자열 넣기
"""
'%s' % '문자열'
"""
print('I am %s' % 'james')


"""
'%d' % '숫자'
"""
print('I am %d years old' % 20)


"""
'%f' % '숫자'
"""
print('%f' % 2.3) # 2.300000
print('%.2f' % 2.3) # 2.30
print('%.3f' % 2.3) # 2.300



# 24.2.2 서식 지정자로 문자열 정렬하기
print('%10s' % 'python') #     python