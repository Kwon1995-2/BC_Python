class People(object):
    def __init__(self, age=0, name=None):
        self.__age = age
        self.__name = name
    def __str__(self):  
        return "Info -- Name:"+self.__name+", age:"+str(self.__age)
    # def __str__(self):
    #     return super().__str__() # 덮어씀 뒤에 것이 실행됨
    
        

p1 = People(29, "John")
print(p1)
