## Rotate a square matrix (n × n) by 90 degrees clockwise
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

## In square matrix length of rows and columns are same
n = len(matrix)

## Transpose 
for i in range(0,n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

## Reverse
for row in matrix:
    row.reverse()

print(matrix)