def linear_search(arr,target):
    n = len(arr)
    found = False
    for i in range(n):
        if arr[i] == target:
            found = True
            return i
    if not found:
        return "Element Not Found"
print(linear_search([1,3,6,2,9],3))