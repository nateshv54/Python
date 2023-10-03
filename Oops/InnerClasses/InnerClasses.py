#InnerClasses
class car:
    def __init__(self) -> None:
        print("Car class Constructor")
        self.cname=203

    class swift:
        def __init__(self) -> None:
            print("swift class constructor")
            self.cid=2023

        def m2(self):
            print(self.cid)
            

i1=car()
k=i1.swift()
k.m2()