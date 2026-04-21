def min_len_sub_array_with_sum_greater_than_equals_k(arr,k):
    left = 0
    cur_sum = 0
    min_len = float("inf")

    for right in range(0,len(arr)):
        cur_sum = cur_sum + arr[right]

        while cur_sum >= k:
            min_len = min(min_len,right-left+1)
            cur_sum = cur_sum - arr[left]
            left += 1

    return min_len

print(min_len_sub_array_with_sum_greater_than_equals_k([2, 3, 1, 2, 4, 3],7))