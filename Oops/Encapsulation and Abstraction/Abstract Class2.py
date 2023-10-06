#Abstract Class
from abc import *
class A(ABC):
    def m1(self):
        return "Hello"
    
    @abstractmethod
    def m2(self):
        return "Hi"

i=A()
print(i.m1())
print(i.m2())

'''
TypeError: Can't instantiate abstract class A with abstract method m2
'''