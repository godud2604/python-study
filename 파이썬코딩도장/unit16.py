# for 변수 in reversed(range(시작, 끝, 증가폭))
for i in reversed(range(10)): # reversed를 사용하여 숫자의 순서를 반대로 뒤집음
    print('Hello, world!', i)


# 반복문의 변수 i를 변경할 수 있을까?
for i in range(10):
    print(i, end = ' ')
    i = 10