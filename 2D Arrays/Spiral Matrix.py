matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

for i in range(0,rows):
    for j in range(0,cols):
        print(matrix[i][j],end=" ")
    for i in range(i+1,rows):
        print(matrix[i][j],end=" ")
    for j in range(i-1,-1,-1):
        print(matrix[i][j])
    