matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

for j in range(0,cols): ## column-wise (as column is fixed)
    for i in range(0,rows): ## row-wise
        print(matrix[i][j],end=" ")
    print()

## Time complexity = O(n^2)