import time 
import pickle 
class Train_Information:
    def __init__(self,tno,tname,arrtime,deptime,date,source,destination):
        self.tno=tno 
        self.tname=tname 
        self.arrtime=arrtime 
        self.deptime=deptime 
        self.date=date 
        self.source=source 
        self.destination=destination 
    def m1(self):
        print('=====Train Information======')
        print("Train_No is:",self.tno)
        print("Train_Name is:",self.tname)
        print("Arrival_Time is:",self.arrtime)
        print("Dept_time is:",self.deptime)
        print("Date is:",self.date)
        print("Source is:",self.source)
        print("Destination is:",self.destination)
print()
print('=====Pickling or Packing=====')
with open("I_HUB_10.txt","wb") as f:
    obj1=Train_Information(1001,"RE","11:00 AM IST","12:30 PM IST","3/10/2023","Hyderabad","Delhi")
    pickle.dump(obj1,f)
    print()
    print("Pickling or Packing operations is done ....")
    obj1.m1()
print()
time.sleep(2)
print("End of an application")