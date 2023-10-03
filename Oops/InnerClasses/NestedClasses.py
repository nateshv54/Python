import time 
class Robot_Class:
	def __init__(self):
		self.name="Chitti"
		self.head=self.HEAD() 
	def m1(self):
		print('Name of robot is:',self.name)
		self.head.talk()
		self.head.chip.think()
	class HEAD:
		def __init__(self):
			self.chip=self.CHIP()
		def talk(self):
				print("Chitti is always talking about sana 24*7")
		class CHIP:
			def think(self):
				print("Chitti is thinking for Sana 48*14")
	  
r1=Robot_Class()
r1.m1()
print()
time.sleep(2)
print("End of an application")