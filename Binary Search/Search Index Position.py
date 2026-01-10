def search_index(arr,target):
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
    return left ## if not found

print(search_index([1,2,3,5,6,8],4))