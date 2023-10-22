#n=int(input("Enter a number: "))
n=5
k=2*(n-1)
for i in range(1,n+1):
    #inner loop for no.of spaces
    for j in range(1,k+1):
        print(end=' ')
    k-=2
    #inner loop for no.of stars
    for j in range(1,i+1):
        print("* ",end='')
    print("\r")

'''
#Rotational pyramid
        * 
      * *
    * * *
  * * * *
* * * * *
'''
z=2*(n-1)
for i in range(1,n+1):
    #inner loop for handling spaces
    for j in range(1,z+1):
        print(end=" ")
    z-=2
    #inner loop for printing numbers
    for j in range(1,i+1):
        print(j,end=" ")
    print('\r')

'''
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
'''
a=2*(n-1)
b=65
for i in range(1,n+1):
    #loop for spaces
    for j in range(1,a+1):
        print(end=" ")
    a-=2
    #innerloop for printing content
    for j in range(1,i+1):
        print(chr(b),end=' ')
        b+=1
    print('\r')  

'''
        A
      B C
    D E F
  G H I J
K L M N O
'''      
c=2*(n-1)
d=1
for i in range(1,n+1):
    for j in range(1,c+1):
        print(end=' ')
    c-=2
    for j in range(1,i+1):
        print(d,end=' ')
        d+=1
    print('\r')
'''     1
      2 3
    4 5 6
  7 8 9 10
11 12 13 14 15 
'''