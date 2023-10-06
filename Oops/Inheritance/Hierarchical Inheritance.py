#Hierarchical Inheritance
class A:
    def __init__(self) -> None:
        self.a=10
    
class B(A):
    def __init__(self) -> None:
        super().__init__()
        self.b=20
    def add(self):
        print("a+b=",self.a+self.b)

class C(A):
    def __init__(self) -> None:
        super().__init__()
        self.c=30
    def mul(self):
        print("a*c=",self.a*self.c)

c=C()
c.mul()
b=B()
b.add()