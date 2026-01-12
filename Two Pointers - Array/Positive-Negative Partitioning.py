def pos_neg(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        while arr[left] < 0 and left < right:
            left += 1
        while arr[right] >= 0 and left < right:
            right -= 1
        if left < right:
            arr[left],arr[right] = arr[right],arr[left]
    return arr
print(pos_neg([12,-7,5,-3,9,-2,-1,6]))