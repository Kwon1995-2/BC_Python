class Calculate :
    #def __init__(self, n, m, c_str):
    # def add(self,a,b): return a+b
    # #def sum(self): return self.n+self.m
    # def sub(self,a,b): return a-b
    # def mul(self,a,b): return a*b
    # def div(self,a,b): return a/b

    def add(self): return self.n+self.m
    def sub(self): return self.n-self.m
    def mul(self): return self.n*self.m
    def div(self): return self.n/self.m

    def calc(self, n, m, c_str):
        self.n = n
        self.m = m
        self.c_str = c_str
        myDict = {'add': Calculate.add, 'sub':Calculate.sub, 'mul':Calculate.mul, 'div':Calculate.div} #'sum':Calculate.sum}
        return myDict[self.c_str](self)

    # def calc(self, n, m, c_str):
    #     self.n = n
    #     self.m = m
    #     self.c_str = c_str
    #     myDict = {'add': Calculate.add, 'sub':Calculate.sub, 'mul':Calculate.mul, 'div':Calculate.div} 
    #     return myDict[c_str](self,n,m)#(self) 


res = Calculate()
print(res.calc(3,5,'mul'))
#print(res.calc(3,5,'sum'))
    
