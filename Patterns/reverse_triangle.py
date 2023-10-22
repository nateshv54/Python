#Reverse simple pyramid
def reverse_simple_pyraid(n):
    c=2*(n-1)
    for i in range(n+1,0,-1):
        for j in range(1,i+1):
            print("*",end=' ')
        for k in range(1,c+1):
            print(end=' ')
        c=c-1
        print('\r')

reverse_simple_pyraid(5)

'''
Output:
* * * * * *
* * * * *
* * * *
* * *
* *
*

'''
def reverse_simple_pyraid_alpha(n):
    c=2*(n-1)
    d=65
    for i in range(n+1,0,-1):
        for j in range(1,i+1):
            print(chr(d),end=' ')
            d+=1
            if(chr(d)=='Z'):
                break
        for k in range(1,c+1):
            print(end=' ')
        c=c-1
        print('\r')

reverse_simple_pyraid_alpha(6)

'''Output:
A B C D E F G
H I J K L M
N O P Q R
S T U V
W X Y
Z [
\ '''