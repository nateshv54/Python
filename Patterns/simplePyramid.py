n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\r")

''''
output:
Enter a number: 5
*
* *
* * *
* * * *
* * * * *

'''
k=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end=" ")
        k+=1
    print("\r")

'''
output:
1
2 3
4 5 6
7 8 9 10 
11 12 13 14 15
'''

#for printing characters
num=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(num),end=" ")
        num+=1
    print("\r")
'''
ouput:
A
B C
D E F
G H I J
K L M N O
'''
    
