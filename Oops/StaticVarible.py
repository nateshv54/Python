#static varible
'''
It can be declared 
-inside construcor using classname
-inside instance method using classname
-inside class using
 =class name
 =cls variable
 
-Inside static method using classname
-Outside the class using classsname
'''
#Note
'''
We cannot access static variable outside the class which are declared inside static method
We can update static variable only after all methods are called.
The updated value doesn't effect the value of static variables inside the class
But updated value will be allowed anywhere inside the class, expect static variable declared
using cls variable                                     '''

#we can delete static variable using del keyword
class c7:
    cname="MegaSoft"
    def __init__(self) -> None:
        c7.pid=101

    def m1(self):
        print("Instance method pid= ",c7.pid)
        c7.padd='afh'
    @classmethod
    def cm1(cls):
        c7.pname='Hello'
        cls.psal=25000
        print(c7.pid)
        print(c7.pname)

    @staticmethod
    def sm1():
        c7.pmobile=24678
        print(c7.padd)

i1=c7()
i1.m1()
c7.sm1()
c7.cm1()
print('cnmae= ',c7.cname)
c7.pid=75000
print(c7.pid)