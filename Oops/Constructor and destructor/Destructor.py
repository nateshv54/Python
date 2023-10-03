#destructor __del__(self)
class c1:
    def __init__(self) -> None:
        print("This is Constructor")

        #deleting callinbg destructor
    def __del__(self):
        print("This is destructor for clearning memory block")

r=c1()
del r
