## Longest sub-array with sum <= k
def longest_sub_array(arr,k):
    left = 0
    cur_sum = 0 
    max_len = 0

    if not arr:
        return 0
    
    for right in range(0,len(arr)):
        cur_sum = cur_sum + arr[right]
        
        while cur_sum > k:
            cur_sum = cur_sum - arr[left]
            left += 1

        max_len = max(max_len,right-left+1)
    
    return max_len

print(longest_sub_array([1,2,1,0,1,1,0],4))