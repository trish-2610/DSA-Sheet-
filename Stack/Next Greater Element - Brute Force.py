def nge(arr,n) -> list:
    result = [-1] * n
    for i in range(n):
        for j in range(i+1,n):
            if arr[j] > arr[i]:
                result[i] = arr[j]
                break
    return result
print(nge([4,10,2,6,13,7,5],7))