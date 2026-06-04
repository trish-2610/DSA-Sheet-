def sort_0s_1s_2s(arr):
    low = 0 
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            ## swap
            arr[mid],arr[low]=arr[low],arr[mid]
            low += 1
            mid += 1
        elif arr[mid] == 2:
            ## swap
            arr[mid],arr[high]=arr[high],arr[mid]
            high -= 1
        else:
            mid += 1
    return arr

print(sort_0s_1s_2s([0,1,0,0,1,2]))