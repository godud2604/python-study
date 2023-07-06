def hello(**kwargs):
  # print('hello ' + kwargs['first'] + " " + kwargs['last'])
  # print('hello', end="")
  for key, value in kwargs.items():
    print(key, end=" ")
    print(value, end=" ")

hello(title="Mr.", first = "Bro", middle = "Dude", last = "Code")