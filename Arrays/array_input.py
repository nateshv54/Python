from array import *
#arr=array('i',[])
n=int(input("Enter the size of array"))
arr=[]
for i in range(n):
    x=int(input())
    arr.insert(i,x)

print(arr)