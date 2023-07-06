# logical operators (논리 연산자)

temp = int(input("what is the temperature outside?: "))

if temp >= 0 and temp <= 30:
  print("the temperature is good today!")
  print("go outside!")
elif temp < 0 or temp > 30:
  print("the temperature is bad today")
  print("stay inside")


if not(temp >= 0 and temp <= 30):
  print("the temperature is bad today")
  print("stay inside")
elif not(temp < 0 or temp > 30):
  print("the temperature is good today!")
  print("go outside!")


