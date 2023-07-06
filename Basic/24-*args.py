def add(*args):
  args = list(args) # tuple은 요소를 변경할 수 없기 때문에, 리스트로 변경한 뒤 업데이트 한다.
  args[0] = 0

  sum = 0
  for i in args:
    sum += i
  return sum

print(add(1, 2, 3, 4, 5, 6))