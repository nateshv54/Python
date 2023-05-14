#BinarySearch
''''Note:The array must be sorted before applying binary serach
'''
def binarysearch(arr,l,h,key):
    if h>=1:
        mid=l+(h-1)//2

        if arr[mid]==key:
            return mid
        elif key < arr[mid]:
            return binarysearch(arr,l,mid-1,key)
        else:
            return binarysearch(arr,mid+1,h,key)
    else:
        return "Element not found in array"
    

arr=[10,20,30,40,60]
key=int(input("Enter element to search "))
print(binarysearch(arr,0,len(arr)-1,key))

