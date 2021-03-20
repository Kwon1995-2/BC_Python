# strVar = 'test'
# test = "파이썬은 쉽다."
# print(type(strVar), type(test), type(10))
##############################################
# class Test:
#   pass
# t=Test()
# print(t)
##############################################
# class Car:
#   def __init__(self, color, speed):
#     self.color = color
#     self.speed = speed
#   def speedUp(self, v):
#     self.speed = self.speed+v
#     return self.speed
#   def speedDown(self, v):
#     self.speed = self.speed-v
#     return self.speed
# c1 = Car('black',50)
# c2 = Car("red",70)
# print("%s %d"%(c1.color, c1.speed))
# print("%s %d"%(c2.color, c2.speed))
# c1.speedDown(10)
# print("%s %d"%(c1.color, c1.speed))
##############################################
# class People:
#   def __init__(self, age=0,name=None):
#     self.__age = age
#     self.__name = name

#   def getAge(self):
#     return self.__age
#   def getName(self):
#     return self.__name
#   def setAge(self, age):
#     self.__age = age
#   def setName(self, name):
#     self.__name = name
# p1 = People(20,"Kim")
# print(p1.getAge(), p1.getName())
# #print(p1.name, p1.__age) __age -> 외부에서 읽거나 변경 못함
##############################################
# class People:
#   def __init__(self, age=0,name=None):
#     self.__age = age
#     self.__name = name
#   def introMe(self):
#     print("Name:",self.__name," age:",str(self.__age))

# class Teacher(People):
#   def __init__(self, age=0, name=None, school=None):
#     super().__init__(age, name)
#     self.__school = school
#   def showSchool(self):
#     print("My school : ", self.__school)
# p1 = People(29, "Lee")
# p1.introMe()

# t1 = Teacher(48, "Kim","HighSchool")
# t1.introMe()
# t1.showSchool()

# class People:
#   def __init__(self, age=0,name=None):
#     self.__age = age
#     self.__name = name

#   def introMe(self):
#     print("Name:",self.__name," age:",str(self.__age))

# class Teacher(People):
#   def __init__(self, age=0, name=None, school=None):
#     super().__init__(age, name)
#     self.__school = school

#   def introMe(self):
#     super().introMe()
#     print("My school : ", self.__school)
  
# class Student(Teacher):
#   def __init__(self, age=0, name=None, school=None, grade = None):
#     super().__init__(age, name, school)
#     self.__grade = grade
#   def introMe(self):
#     super().introMe()
#     print("Grade : ", self.__grade)

# p1 = People(29, "Lee")
# p1.introMe()

# t1 = Teacher(48, "Kim","HighSchool")
# t1.introMe()

# s1 = Student(17, "Park","HighSchool",2)
# s1.introMe()
##############################################
# class Car():
#   def __init__(self, make, model, year):
#     self.make=make
#     self.model = model
#     self.year = year
#     self.odometer_reading = 0
  
#   def get_car_name(self):
#     long_name = str(self.year)+' '+self.make+' '+self.model
#     return long_name.title()

# class ElectricCar(Car):
#   def __init__(self, make, model, year):
#     super().__init__(make, model, year)
#     self.battery = Battery()

# class Battery(): #ElectricCar 클래스의 인스턴스인 Battery를 별도의 클래스로 만듦
#   def __init__(self, batter_size=70):
#     self.batter_size = batter_size
#   def describe_battery(self):
#     print("This car has a "+str(self.batter_size)+"-kWh battery.")

# my_tesla = ElectricCar('tesla','model s',2016)
# print(my_tesla.get_car_name())
# my_tesla.battery.describe_battery()
##############################################
# class Korean(object):
#   def greeting(self):
#     print("안녕하세요")

# class American(object):
#   def greeting(self):
#     print("Hello")

# def sayhello(people):
#   people.greeting()

# Kim = Korean()
# John = American()
# sayhello(Kim)
# sayhello(John)
##############################################
# class Machine: # == class Machine(object)
#   sNumber = 0
#   def __init__(self):
#     Machine.sNumber += 1
#     self.number = Machine.sNumber
# m1 = Machine()
# print(m1.sNumber)
# m2 = Machine()
# print(m2.sNumber)
##############################################
class People(object):
  def __init__(self, age=0, name=None): #오버라이딩
    self.__age = age
    self.__name = name
  def __str__(self):
    #return super().__str__()
    return "Info -- Name : "+self.__name+", age : "+str(self.__age)

p1 = People(29, "John")
print(p1)