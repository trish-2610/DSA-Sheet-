matrix = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
]

target = 5
found = False
rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == target:
            print(f"Found at index : ",{i,j})
            found = True 
            break
    if found:
        break
if not found:
    print("Element not found")

## TC = O(n x m) ## Slow
## we can implement it using binary search also (code available in binary search folder) ## TC = O(n log m)