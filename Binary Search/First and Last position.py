def first_position(arr,target):
    left = 0
    right = len(arr) - 1
    ans = -1 ## stores index
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            ans = mid
            right = mid - 1 ## search on left side
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans 

def last_position(arr,target):
    left = 0
    right = len(arr) - 1
    ans = -1 ## stores index
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            ans = mid
            left = mid + 1 ## search on right side
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return ans 

print(first_position([1,3,3,3,3,4],3))
print(last_position([1,3,3,3,3,4],3))