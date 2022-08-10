class Organism:
  
  alive = True

class Animal(Organism):

  def eat(self):
    print("This animal is eating")

class Dog(Animal):

  def back(self):
    print("This dog is back")

dog = Dog()
print(dog.alive)
dog.eat()
dog.back()