def find_avg(arr,k):
    
    if not arr or k > len(arr):
        return []
     
    result = []
    cur_sum = sum(arr[:k])
    result.append(cur_sum/k)

    for i in range(k,len(arr)):
        cur_sum = cur_sum + arr[i] - arr[i-k]
        result.append(cur_sum/k)
    
    return result

print(find_avg([1,2,3,4,7],3))