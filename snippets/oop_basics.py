class Student:
  def __init__(self, name, field):
    self.name = name
    self.field = field

  def introduce(self):
    return "Hi, I'm " + self.name + " and I study " + self.field


s1 = Student("Ram", "Machine Learning")
print(s1.introduce())
