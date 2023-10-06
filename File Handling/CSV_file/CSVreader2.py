import time,csv
f1=open("c1.csv","r")
s1=csv.reader(f1)
for x1 in s1:
    for x2 in x1:
        print(x2,end=" ")
