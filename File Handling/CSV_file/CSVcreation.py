import csv
with open("c1.csv","w",newline="") as f:
    s1=csv.writer(f)
    s1.writerow(['pid','pname','price','company'])
    n=int(input("Enter the no.of rows"))
    for x1 in range(n):
        pid=int(input("Enter the pid"))
        pname=input("Enter the pname: ")
        price=float(input("Enter the price: "))
        company=input("Enter the company")
        s1.writerow([pid,pname,price,company])
    print("A csv file is created successfully..")
