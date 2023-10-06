#Access Modifiers
class A:
    #public
    eid=1001
    #protected
    _pid=20
    #private
    __pname="ROM"
    def name(self):
        __a=10
        print(__a)

i=A()
print(i.eid)
print(i._pid)
#print(i.__pname)
i.name()