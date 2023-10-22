'''F'ind a peak element which is not smaller than its neighbours
Note: For corner elements, we need to consider only one neighbor. 

Example:

Input: array[]= {5, 10, 20, 15}
Output: 20
Explanation: The element 20 has neighbors 10 and 15,
both of them are less than 20.
'''

def findpeak(arr,n):
    if(n==1):
        return arr[0]
    if(arr[0]>=arr[1]):
        return arr[0]
    if(arr[n-1]>= arr[n-2]):
        return arr[n-1]
    #check for every other element
    for i in range(n):
        if(arr[i]>=arr[i-1] and arr[i]>=arr[i+1]):
            return arr[i]
    
arr=[1,2,19,18,10]
n=len(arr)
print("Peak element is is", findpeak(arr,n))

'''Time complexity : O(n)
 Space Complexity(SC): O(1), 
    no extra space is needed, so SC is constant'''