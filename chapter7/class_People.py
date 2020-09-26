class People :
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name
    def introMe(self):
        print("Name :",self.__name, "age :", str(self.__age))

class Teacher(People):
    def __init__(self, age=0, name=None, school=None):
        super().__init__(age, name)
        self.school = school
    def showSchool(self):
        print("MySchool is", self.school)

class Student(People):
    def __init__(self, age=0, name=None, grade=None):
        super().__init__(age, name)
        self.__grade = grade
    def introMe(self):
        super().introMe()
        print("Grade : ", self.__grade)

# Student = Teacher(20, 'Simon')
# print(Student.introMe())

p1 = People(29, "Lee")
p1.introMe()

s1 = Student(17,"Park",2)
s1.introMe()

