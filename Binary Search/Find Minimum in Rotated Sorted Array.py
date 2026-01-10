def find_min(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[right] : ## right half is rotated , so min lies here
            left = mid + 1
        else:
            right = mid
    return arr[left] ## or arr[right]
## loop stops when left == right
print(find_min([5,1,2,3,4]))