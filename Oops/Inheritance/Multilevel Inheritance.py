#Multilevel Inheritance
class A:
    def __init__(self) -> None:
        self.a=10
    def value(self):
        print("Value of a is",self.a)

class B(A):
    def __init__(self) -> None:
        super().__init__()
        self.b=20
    def value2(self):
        print("Value of B is ",self.b)

class C(B):
    def __init__(self) -> None:
        super().__init__()
        self.c=30
    def value3(self):
        print("value of C is",self.c)
    def add(self):
        print("A+B+C = ",self.a+self.b+self.c)

a=A()
a.value()
b=B()
b.value2()
c=C()
c.value3()
c.add()