import csv
f1=open("c1.csv",'r')
s1=csv.reader(f1)
print(*s1)
