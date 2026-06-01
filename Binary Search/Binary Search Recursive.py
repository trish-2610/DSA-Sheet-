def binary_search(arr,target,left,right):

    if left > right:
        return -1 ## Not found 

    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid 
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,right)
    else:
        return binary_search(arr,target,left,mid-1)
    
arr = [1,3,5,7,9]
print(binary_search(arr,7,0,len(arr)-1))

## TC = O(log n)
## Sc = O(log n)