from Class_objects_inheritance import Multiply

class Child1(Multiply):
    p = 20
    q = 30

    def __init__(self, x, y):
        super().__init__(x, y)
    def add(self):
        return self.p + self.q

    def countall(self):
        print("The total of addition and multiplication is : ", self.add() + self.multiplication())
        #return self.add() + self.multiplication()


C1 = Child1(10, 20)
print(C1.multiplication())
print(C1.add())
C1.countall()
print(C1.a)

