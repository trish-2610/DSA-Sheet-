def first_last_occurrence(arr,target):

    def find(arr,target,is_first):
        left = 0
        right = len(arr) - 1
        ans_find = -1
        while left <= right:
            mid = left + (right-left) // 2
            if arr[mid] == target:
                ans_find = mid 
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans_find
    ans = []
    ans.append(find(arr,target,True))
    ans.append(find(arr,target,False))
    return ans 

print(first_last_occurrence([1,2,2,2,4,5],2))

## checking changes
