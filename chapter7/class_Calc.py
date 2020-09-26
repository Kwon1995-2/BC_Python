class Calc:
    count = 0
    def add(self, a=0, b=0):
        self.a = a
        self.b = b
        self.count += 1
        return self.a + self.b
    
    def minus(self, a, b):
        if a == 0 or b == 0:
            return a-b, self.count
        else:
            return a-b

obj = Calc()
print(obj.minus(3, 0))
print(obj.minus(3,1))
print(obj.add(1,2))
print(obj.count, Calc.count) #인스턴스  변수 obj.count는 변하지만 클래스 변수 Calc.count는 변하지 않음
