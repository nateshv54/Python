#Instance Method(Non-static method)
''' It is used for business logic
 -It can be only accesses through object reference variable
 We can take any varibale as parmeter in instance method but self as parameter 
 is a good practice'''

class ihub:
    def __init__(self):
        print("Constructor")
    def m1(self):
        return "Hello Instance method"
    
i1=ihub()
print(i1.m1())