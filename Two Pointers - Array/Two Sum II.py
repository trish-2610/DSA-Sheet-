def twoSum(arr,target):
    left = 0
    right = len(arr) - 1
    while left < right:
        cur_sum = arr[left] + arr[right]
        if cur_sum == target:
            return [left+1,right+1] ## index from 1 not 0
        elif cur_sum < target:
            left += 1
        else:
            right -= 1
    return -1 
print(twoSum([1,2,4,9],3)) ## calling funcionss