def searchRange(arr, target):

        def find(arr,target,find_first):
            left = 0 
            right = len(arr) -1
            ans_find = -1

            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] == target:
                    ans_find = mid
                    if find_first:
                        right = mid - 1 ## search on left
                    else:
                        left = mid + 1 ## search on right
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return ans_find
        ans = []
        ans.append(find(arr,target,True))
        ans.append(find(arr,target,False))
        return ans
print(searchRange([1,3,3,3,3,4],3))