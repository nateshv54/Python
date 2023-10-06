#Multiple Inheritance
'''Child classs inherits properties and methods from multiple classses'''

class A:
    def __init__(self) -> None:
        self.a=10

class B:
    def __init__(self) -> None:
        self.b=20
class C:
    def __init__(self) -> None:
        self.c=20

class D(A,B,C):
    def __init__(self) -> None:
        super().__init__(self.b,self.c,self.a)
        self.d=30
        print("Addition is ",self.a+self.d)

d=D()