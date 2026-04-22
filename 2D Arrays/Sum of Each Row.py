matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

for i in range(0,rows):
    row_sum = 0
    for j in range(0,cols):
        row_sum += matrix[i][j]
    print(row_sum)

## TC = O(n^2)