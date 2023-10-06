#Abstract Methods
from abc import *
class  A:
    @abstractmethod
    def m1(self):
        print("Abstract method")

r=A()
r.m1()