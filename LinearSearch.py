#Linear Search 

def LinearSearch(arr, key):
    for i in range(len(arr)):
        if(arr[i]==key):
            return 'Element found at index', i
    return "Element not found"    
    
arr=[1,3,45,21,66]
key=int(input("Enter key value to search: "))
print(LinearSearch(arr,key))

'''Time Complexity: O(n)
Auxiliary Space: O(1) as no extra space was needed.'''

