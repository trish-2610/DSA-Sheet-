def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j
        ## swap 
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

print(selection_sort([5,2,9,1,5]))