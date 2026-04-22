matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

## code complexity O(n^2)
for i in range(0,rows):
    for j in range(0,cols):
        if i == j: ## checks diagonal elements
            print(matrix[i][j],end=" ")

## another way with less complexity O(n)
for i in range(0,rows):
    print(matrix[i][i],end=" ")