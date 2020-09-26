class Person :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)

class Employee(Person):
    def __init__(self, name=None,  age=0, emID=None):
        super().__init__(age, name)
        self.emID = emID
    def getID(self):
        #return self.emID
        print(self.emID)

Kim = Employee("동양", 65, 2019)
#print(Kim.getName)
# Kim.getName()
# Kim.getAge()
# print(Kim.getID())
#print(Kim.getName(), Kim.getAge(), Kim.getID())
Kim.getName(), Kim.getAge(), Kim.getID()



    