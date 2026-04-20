def min_sum_sub_array(arr,k):
    cur_sum = sum(arr[:k])
    min_sum = sum(arr[:k])

    if not arr or k > len(arr): ## empty of greater
        return 0
    
    for i in range(k,len(arr)):
        cur_sum = cur_sum + arr[i] - arr[i-k]
        min_sum = min(min_sum,cur_sum)
    
    return min_sum

print(min_sum_sub_array([2,1,5,1,3,2],4))