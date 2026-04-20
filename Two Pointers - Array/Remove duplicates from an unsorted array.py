def remove_duplicates_unsorted(arr):
    result_arr = [] ## using extra space
    for item in arr:
        if item not in result_arr:
            result_arr.append(item)
    return result_arr

print(remove_duplicates_unsorted([1,2,1,3,3,-1,-1,-4,2,4,5,5]))

## another way - return list(set(arr))