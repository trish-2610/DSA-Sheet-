def longest_sub_array_of_size_k(arr,k):
    left = 0
    cur_sum = 0
    max_len = 0

    for right in range(0,len(arr)):
        cur_sum = cur_sum + arr[right] ## adds element

        while cur_sum > k:
            cur_sum = cur_sum - arr[left] ## remove element
            left += 1 ## moves left pointer

        if cur_sum == k:
            max_len = max(max_len,right-left+1)

    return max_len

print(longest_sub_array_of_size_k([4, 1, 1, 1, 2, 3, 5],5))