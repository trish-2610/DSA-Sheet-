def search_rotated(arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        ## check which half is sorted 
        if arr[left] <= arr[mid]:
            ## left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            ## right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
print(search_rotated([4,5,6,1,2,3],2)) 



