def two_sum_unsorted(arr,target):
    n = len(arr)
    for i in range(n): 
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                return True
    return False

print(two_sum_unsorted([0,-1,2,-3,1],-2))

## Another way :
## 1st sort the array , then apply two pointers (binary search) 