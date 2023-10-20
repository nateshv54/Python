#Compare Versions
'''
You are given two versions number A and B.Your task is to compare them and which one of them 
is a newer version.

Input:
2
1.2.4
1.2.3
10.2.2
10.2.2

Output:
1
0

Explanation:
For the first test case, the first two parts of both the strings are the same but the third part of the 1st version is bigger than the 2nd version.
Hence our answer is 1. For the second test case, both the versions are identical here, so the answer will be 0.
'''
from os import *
from sys import *
from collections import *
from math import *

def compareVersions(a, b):
    #Write your code here
    a=list(map(int,a.split(".")))
    b=list(map(int,b.split(".")))
    length=len(a)-len(b)

    if length>0:
        b.extend([0]*length)
    else:
        a.extend([0]*abs(length))

    
    for i in range(len(a)):
        if a[i]>b[i]:
            return 1
        if a[i]<b[i]:
            return -1

    return 0

if __name__=="__main__":
    a=input("Enter A version: ")
    b=input("Enter B version: ")
    print(compareVersions(a,b))