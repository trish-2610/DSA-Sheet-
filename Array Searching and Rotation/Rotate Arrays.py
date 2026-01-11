def rotation(arr,k,is_left):
    k = k % len(arr)
    if is_left:
        arr = arr[k:] + arr[:k]
    else:
        arr = arr[-k:] + arr[:-k]
    return arr
print(rotation([1,2,3,4,5],1,True)) ## left rotation 
print(rotation([1,2,3,4,5],1,False)) ## right rotation