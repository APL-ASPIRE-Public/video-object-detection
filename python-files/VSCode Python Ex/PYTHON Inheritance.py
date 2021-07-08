# What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?
class Student(Person):
    
# What is the correct syntax to execute the printname method of the object x?
class Person:
 def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()


