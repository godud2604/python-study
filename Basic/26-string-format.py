animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))
print("The {item} jumped over the {animal}".format(animal="cow", item="moon"))

text = "The {} jumped over the {}"
print(text.format(animal, item))


name = "Bro"

# format( ) 함수를 이용하여 포맷팅 할때 치환할 값의 전체 자리수 또는 정렬 방식등을 추가할 수 있습니다.
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}".format(name)) # 치환하는 값에 10칸 자리수가 생성 
print("Hello, my name is {:<10}".format(name)) # 10칸 자리수 주고 왼쪽 정렬 
print("Hello, my name is {:>10}".format(name)) # 10칸 자리수 주고 오른쪽 정렬 
print("Hello, my name is {:^10}".format(name))


number = 1000
print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number pi is {:X}".format(number))
print("The number pi is {:E}".format(number))