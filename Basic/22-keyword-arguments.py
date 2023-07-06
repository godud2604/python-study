# keyword paremeter 
# => 함수 호출 시, 인자의 값 뿐만 아니라 그 이름까지 명시적으로 지정해서 전달

def hello(first, middle, last):
  print('Hello ' + first + " " + middle + " " + last)

hello(last = 'Bro', middle = 'Dude', first = 'Code')