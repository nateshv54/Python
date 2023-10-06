class Train_information:
    def __init__(self,tno,tname,arrtime,deptime,date,source,destination) -> None:
        self.tno=tno
        self.tname=tname
        self.arrtime=arrtime
        self.deptime=deptime
        self.date=date
        self.source=source
        self.destination=destination
    def m1(self):
        print("Train Information")
        print("Train No: ",self.tno)
        print("Train Name: ",self.tname)
        print("Arrtime is : ",self.arrtime)
        print("Date is :",self.deptime)
        print("Date is: ",self.date)
        print("Source is: ",self.source)
        print("Destination is: ",self.destination)