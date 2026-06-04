def counting_sort(arr):
    ## Step-1 : find max
    max_num = max(arr)

    ## Step-2 : Create count array
    count_arr = [0] * (max_num+1)

    ## Step-3 : Fill count_arr with count(index-wise)
    for num in arr:
        count_arr[num] += 1
    
    result = []

    ## Step-4 : Fill result array with index and count
    for idx,count in enumerate(count_arr):
        result.extend([idx]*count)

    return result

print(counting_sort([2,4,4,3,1,7]))