# with..as 구문 
# 파일 스트림을 다루는데, 파일을 열고 해당 구문이 끝나면 자동으로 파일이 닫히게 된다.
# => with open(파일 경로, 모드) as 파일 객체:

try:
  with open('sample.txt', 'w') as file:
    file.write('its simple code')
except FileNotFoundError:
  print("That file was not found :(")


