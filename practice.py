def bubble_sort(arr):
    n = len(arr)
    swaps_count = 0
    for i in range(0,n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                ## swap
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swaps_count += 1
    return arr,swaps_count
    
print(bubble_sort([4,6,2,1,5]))
