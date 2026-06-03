def floor_ceil(arr,target):
    left = 0
    right = len(arr) - 1
    floor = None 
    ceil = None

    while left <= right:
        mid = left + (right-left) // 2
        if arr[mid] == target:
            return arr[mid],arr[mid] ## element found (floor and ceil is same as target)
        elif arr[mid] < target: ## this could be possible floor (if target not found)
            floor = arr[mid]
            left = mid + 1 
        else: ## this could be possible ceil (if target not found)
            ceil = arr[mid]
            right = mid - 1
    return floor,ceil

print(floor_ceil([2,4,6,8,10],7))
