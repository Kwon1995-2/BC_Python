class Deposit:
    def __init__(self, initial, interest, n):
        self.initial = initial
        self.interest = interest
        self.n = n

    def profit(self):
        return self.initial*(1+self.interest)**self.n

Dep = Deposit(100,3.5,7)
print(int(Dep.profit()))


