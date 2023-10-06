#Abstract Class
from abc import *
class A(ABC):
    def m1(self):
        return "Hello€"

i=A()
print(i.m1())
