"""예제의 Teacher class에서 People 클래스의 
__init__()를 호출하지 않고 부모 클래스의 age, name 
속성을 이용할 수 있는가?"""

class People :
    def __init__(self, age=0, name=None): #private 함수
        self.age = age
        self.name = name
    def introMe(self):
        print("Name :",self.name, "age :", str(self.age))

class Teacher(People):
    def __init__(self, age=0, name=None, school=None):
        super().__init__(age, name)
        self.school = school
    def showSchool(self):
        print("MySchool is", self.school)

Student = Teacher(20, 'Simon')
print(Student)
print(Student.introMe())
print(Student.age) 
# self.__age -> 접근 불가
# self.age -> 접근 가능
