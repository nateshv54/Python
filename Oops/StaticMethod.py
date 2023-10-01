#Static method
'''Note: Only method in oops can execute without taking any parameters'''
class c4:
    def __init__(self) -> None:
        print("Constructor method is defaultly exected when object is created")
    @staticmethod
    def s1():
        return "Hellow static method"
    
print(c4.s1())