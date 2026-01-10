def binary_search(arr,target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        ## if mid is matched to target
        if arr[mid] == target:
            return mid
        elif arr[mid] < target: ## right
            left =  mid + 1
        else: ## left
            right = mid - 1
    return -1 ## if not found

print("Index of target element = ",binary_search([1,2,3,5,6,8],6))