# 1. pass : 실행할 코드가 없는 것으로 다음 행동을 계속해서 진행합니다.
# 2. continue : 바로 다음 순번의 loop를 수행합니다.
# 3. break : 반복문을 멈추고 loop 밖으로 나가도록합니다.

# while True:
#   name = input('enter your name: ')
#   if name != "":
#     break

phone_number = "123-456-7890"

for i in phone_number:
  if i == "-":
    continue
  print(i, end="")

for i in range(1, 21):
  if i == 13:
    pass
  else:
    print(i)