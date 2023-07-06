# Overriding(오버라이딩): 재정의, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
# Overloading(오버로딩): 동일한 이름의 함수를 매개변수에 따라 다른 기능으로 동작

class Animal:

  alive = True

  def eat(self):
    print("This animal is eating")

  def slumber(self):
    print("slumber")

class Rabbit(Animal):
  def run(self):
    print("run")
class Fish(Animal):
  def swim(self):
    print("swim")
class Hawk(Animal):
  def fly(self):
    print("fly")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()