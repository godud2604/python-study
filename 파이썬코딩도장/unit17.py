i = 0

while i < 10:
    print('Hello, world!', i)
    i += 1




import random # random 모듈을 가져옴

a = 0
while a != 3: # 3이 아닐 때 계속 반복
    a = random.randint(1, 6) # randint를 사용하여 1과 6 사이의 난수를 생성 
    print(a)
    



dice = [1, 2, 3, 4, 5, 6]

# random.choice 함수는 시퀀스 객체를 받으므로, 리스트뿐만 아니라 튜플, range, 문자열 등을 넣어도 된다.
b = random.choice(dice) 
print('b', b)