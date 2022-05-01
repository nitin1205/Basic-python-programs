#using loop
def BinarySearch(arr,key):
    l=0
    h=len(arr)-1
    while(l<=h):
        mid=(l+h)//2
        if(key==arr[mid]):
            return mid
        elif(key<arr[mid]):
            h=mid-1
        else:
            l=mid+1
    return "Not found"

#using recursion
def RBinSearch(arr,l,h,key):
    if(l<=h):
        mid=(l+h)//2
        if(key==arr[mid]):
            return mid
        elif(key<mid):
            return RBinSearch(arr,l,mid-1,key)
        else:
            return RBinSearch(arr,mid+1,h,key)
    else:
        return "Not Found"

arr = [4,6,2,7,89,3,9,4,56]    
print(BinarySearch(arr,76))
print(RBinSearch(arr,0,len(arr)-1,76))
        