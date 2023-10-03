import time 
class I_HUB:
	def __init__(self):
		I_HUB.A1=1500
		print(I_HUB.A1) 
	def m1(self):
		I_HUB.A1=15000
		print(I_HUB.A1)
	@classmethod 
	def m2(cls):
		I_HUB.A1=150000
		print(I_HUB.A1)
	      
	@staticmethod 
	def m3():
		#I_HUB.A1=1500004
		print(I_HUB.A1)
i1=I_HUB()
print()
i1.m1()
print()
i1.m2()
print()
i1.m3()
print()
I_HUB.A1=1578493923
print("The current A1 value is:",I_HUB.A1)
print()
time.sleep(2)
print("End of an application")
