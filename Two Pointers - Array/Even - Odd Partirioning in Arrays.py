def even_odd(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        while arr[left] % 2 == 0 and left < right:
            left += 1
        while arr[right] % 2 != 0 and left < right:
            right -= 1
        if left < right:
            arr[left],arr[right] = arr[right],arr[left]
    return arr
print(even_odd([1,5,4,6,7,9,8,2]))