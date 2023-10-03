#Default Variable
'''self is a default variable.It is used to declare instance variable inside the constructor'''
class c8:
    def __init__(self) -> None:
        self.pid=201
    def m2(self):
        print(self.pid)

i1=c8()
i1.m2()