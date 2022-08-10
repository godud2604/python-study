class Prey:
  
  def flee(self):
    print("flee")

class Predator:

  def hunt(self):
    print("This animal is hunting")

class Rabbit(Prey):
  pass

class Hawk(Predator):
    pass


class FourCal:
  def setdata(self, first, second):
      self.first = first
      self.second = second
  def add(self):
      result = self.first + self.second
      return result
  def mul(self):
      result = self.first * self.second
      return result
  def sub(self):
      result = self.first - self.second
      return result
  def div(self):
      result = self.first / self.second
      return result

