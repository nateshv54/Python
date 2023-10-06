#Duck typing
class Bird:
    def fly(self):
        print("Fly with wings")

class Airplane:
    def fly(self):
        print("Fly with fuel")

class Chopper:
    def fly(self):
        print("Fly with fans")

for obj in Bird(),Airplane(),Chopper():
    obj.fly()