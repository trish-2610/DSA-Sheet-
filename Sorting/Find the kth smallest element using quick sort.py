## arr = [3,4,7,1,2,8]
## after sorting , arr = [1,2,3,4,7,8]
## if k = 3 
## the kth smallest element = 3

## quick sort function
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    mid = [x for x in arr if x == pivot]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

## smallest element function
def kth_smallest(arr,k):
    sorted_arr = quick_sort(arr)
    return sorted_arr[k-1] ## index = 3-1 -> 2 

print(kth_smallest([3,4,7,1,2,8],3)) 