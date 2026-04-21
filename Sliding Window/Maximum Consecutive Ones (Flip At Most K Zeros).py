def max_consecutive_ones(arr,k):
    left = 0
    max_len = 0
    zero_count = 0

    for right in range(0,len(arr)):

        if arr[right] == 0: ## counts zeros 
            zero_count += 1

        while zero_count > k: ## if condition is invalid
            if arr[left] == 0: ## reduces zeros other while loop will keep on working
                zero_count -= 1
            left += 1 ## shrink from left
        
        max_len = max(max_len,right-left+1)
    return max_len

print(max_consecutive_ones([1,1,0,0,1,1,1,0,1],2))