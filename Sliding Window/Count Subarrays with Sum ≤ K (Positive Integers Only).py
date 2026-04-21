## Count Sub-arrays with Sum ≤ K (Positive Integers Only)
# arr = [1, 2, 1, 0, 1]
# k = 3
# O/P = [1], [1,2], [2], [2,1], [1], [1,0], [1,0,1], [0], [0,1], [1]

def count_sub_arrays(arr,k):
    left = 0
    cur_sum = 0 
    count = 0

    for right in range(0,len(arr)):
        cur_sum = cur_sum + arr[right]

        while cur_sum > k:
            cur_sum = cur_sum - arr[left]
            left += 1
      
        count += 1

    return count

print(count_sub_arrays([1, 2, 1, 0, 1],3))