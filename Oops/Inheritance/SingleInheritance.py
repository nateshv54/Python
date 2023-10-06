#single inheritance
class A:
    def __init__(self) -> None:
        self.a=10
    def value(self):
        print( "Value is",self.a)
    
class B(A):
    def __init__(self) -> None:
        #super function is used to access methods of immediate parent class
        super().__init__()
        self.b=20
    def add(self):
        print("Addition is ",self.a+self.b)

b=B()
b.add()
#parent class
a=A()
a.value()
