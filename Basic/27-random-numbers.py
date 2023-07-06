import random

x = random.randint(1, 6)
y = random.random()

print(x)
print(y)

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList) 

print(z) 

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]

random.shuffle(cards) # 시퀀스를 섞어놓는 함수

print(cards)