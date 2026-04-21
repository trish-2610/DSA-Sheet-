## Count Sub-arrays of Size K with Sum > X
def count_sub_arrays(arr,k,x):

    if not arr or k > len(arr):
        return 0
    
    count = 0 
    cur_sum = sum(arr[:k]) ## sum of first k elements
    
    if cur_sum > x:
        count += 1

    for i in range(k,len(arr)):
        cur_sum = cur_sum + arr[i] - arr[i-k]
        if cur_sum > x:
            count += 1
    
    return count

print(count_sub_arrays([2,5,1,8,2,9,1],3,10))