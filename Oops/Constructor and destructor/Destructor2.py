class employee:
    def __init__(self) -> None:
        print("Employee constructor is created")
    
    #calling destructor
    def __del__(self):
        print("Destructor is called to end open objects")



def createobj():
    obj=employee()
    return obj

obj=createobj()
print("program end")