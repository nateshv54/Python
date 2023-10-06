import time 
from abc import *
class I_HUB_1(ABC):
    @abstractmethod 
    def m1(self):
        pass 
class I_HUB_2(I_HUB_1):
    def m1(self):
        return "Welcome to IHUB IT services"
class I_HUB_3(I_HUB_1):
    def m1(self):
        return "Welcome to IHUB for Web application development"
class I_HUB_4(I_HUB_1):
    def m1(self):
        return "Welcome to IHUB for ERP application development"
i1=I_HUB_2()
i1.m1()
print()
i2=I_HUB_3()
i2.m1()
print()
i3=I_HUB_4()
i3.m1()
print()
time.sleep(2)
print('End of an application')

''''



End of an application
'''