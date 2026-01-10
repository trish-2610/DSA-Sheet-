def peak_index(arr):
    n = len(arr)
    if n == 1: return 0
    if arr[0] > arr[1] : return 0
    if arr[n-1] > arr[n-2] : return n-1
    left = 1
    right = n-2
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
            return mid
        elif arr[mid - 1] < arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1
print(peak_index([1,2,1,3,5,6,4]))