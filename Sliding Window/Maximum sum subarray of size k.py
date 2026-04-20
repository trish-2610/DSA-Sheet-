def max_sum_sub_array(arr,k):
    cur_sum = sum(arr[:k])
    max_sum = sum(arr[:k])

    if not arr or k > len(arr):
        return 0 

    for i in range(k,len(arr)):
        cur_sum = cur_sum + arr[i] - arr[i-k]
        max_sum = max(max_sum,cur_sum)

    return max_sum

print(max_sum_sub_array([3,2,1,4,5],2))