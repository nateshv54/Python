#Class Method
'''Note: For class method we can take any variable as parameter but cls is 
good practice'''

class c3:
    def __init__(s) -> None:
        print("Constructor")
    def i1(s):
        return "Instance method"
    @classmethod
    def cm1(cls):
        return "Class method1"
    @classmethod
    def cm2(cls):
        return "class method2"
    
i1=c3()
print(i1.i1())
print("Calling classmethod using class name\n",c3.cm1())