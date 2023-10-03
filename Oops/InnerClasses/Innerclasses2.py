class c4:
    def __init__(self) -> None:
        self.name="chitti"
        self.head=self.Head()
    def m1(self):
        print("Name of robot",self.name)
        self.head.talk()
        self.head.chip.think()
    class Head:
        def __init__(self) -> None:
            self.chip=self.Chip()
        def talk(self):
            print("Custom words")
        class Chip:
            def think(self):
                print("Charge and speed")

r1=c4()
r1.m1()