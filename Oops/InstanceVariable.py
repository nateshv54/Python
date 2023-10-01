#Instance Variable
'''Inside the constructor
Inside instance method
Outside the class using object reference variable'''
#instance variable deleted using del

class c6:
    def __init__(self) -> None:
        self.eid=100
        self.ename="paul allen"
        self.e2=20
        self.e4=30
        #deleting
        del self.e2

    def im1(self):
        #instance method can access instance varible values from constructor,
        #where as class and static method doesn't access
        print(self.eid)
        self.pid=200
        self.p5=5
        self.pname="Paul Allen"
        print(self.pid)
        del self.e4

i1=c6()
i1.im1()
#__dict__ is a magic method used print instance variables in form of dictionary
print(i1.__dict__)
print("Instane varibale Outside the class ** using object reference varibale")
i1.sid=1011


# deleting instance varibale
del i1.p5
print(i1.__dict__)

print("Printing instance varibale values inside class")
print(i1.ename)
print(i1.pid)

#Updating instance varible values
i1.eid=201
print(i1.__dict__)
