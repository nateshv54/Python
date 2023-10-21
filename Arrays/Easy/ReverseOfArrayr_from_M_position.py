#Reverse of array
'''
Given a array arr and position m, we have to print the
 reverse of array after position m and return the whole array'''

from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    # Write your code here.
    arr[m+1:len(arr)]=reversed(arr[m+1:len(arr)])
    return arr
#better to think of other approach

if __name__=="__main__":
    arr=[1,4,6,65,7,8,0]
    print(reverseArray(arr,3))