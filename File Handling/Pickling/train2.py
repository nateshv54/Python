from train1 import Train_information
import pickle
f1=open("train_info.txt","wb")
n=int(input("Enter no.of rows: "))
for x1 in range(n):
    tno=int(input("Enter tno: "))
    tname=int(input("Enter tname: "))
    arrtime=input("Enter arrtime: ")
    depttime=input("Enter depttime: ")
    date=input("Enter the date")
    source=input("Enter source")
    destination=input("Enter destination")
    t1=Train_information(tno,tname,arrtime,depttime,date,source,destination)
    pickle.dump(t1,f1)
    print()
print("Pickling is done")
f1.close()
