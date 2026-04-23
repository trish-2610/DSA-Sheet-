def search_sorted_matrix(row,target):
    left = 0
    right = len(row) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if row[mid] == target:
            return True
        elif row[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

matrix =[
    [1,3],
    [2,4]
]
for row in matrix: ## passing one row at a time ( as we can't whole matrix at once)
    if search_sorted_matrix(row,1):
        print("Element found")
        break
else:
    print("Element not found")

## TC = O(n log m)