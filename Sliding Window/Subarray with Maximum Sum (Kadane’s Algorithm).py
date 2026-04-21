## Sub-array with Maximum Sum (Kadane’s Algorithm)
## Maximum Sum sub-array

def kadane_algo(arr):
    cur_sum = arr[0]
    max_sum = arr[0]

    for i in range(1,len(arr)):
        cur_sum = max(cur_sum + arr[i] , arr[i])
        max_sum = max(max_sum,cur_sum)

    return max_sum

arr = [-2,1,-3,4,-1,2,1,-5,4]
print(kadane_algo(arr))

## if cur_sum is negative --> Restart
## else continue 