n1=int(input())
n2=int(input())
n3=int(input())

print("Greatest of three numbers",n1 if(n1>n2 and n1>n3) else(n2 if(n2>n1 and n2>n3)else n3))