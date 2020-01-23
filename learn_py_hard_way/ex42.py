class Animal(object):
  
  def __init__(self, name):
    self.name = name
  
class Dog(Animal):
  
  def __init__(self, name):
    self.name = name

class Cat(Animal):
  
  def __init__(self, name):
    self.name = name
    
class Person(object):
  
  def __init__(self, name):
    self.name = name
    self.pet = None
    
class Employee(Person):
  
  def __init__(self, name, salary):
    super(Employee, self).__init__(name)
    self.salary = salary
    
class Fish(object):
  
  def __init__(self, name):
    self.name = name
  
class Salmon(Fish):
  
  def __init__(self, name):
    self.name = name

class Halibut(Fish):
  
  def __init__(self, name):
    self.name = name
  
rover = Dog("Rover")

satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish("Flipper")

crouse = Salmon("Crouse")

harry = Halibut("Harry")

print(frank.name)

print(satan.name)

print(flipper.name)
