matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

rows = len(matrix)
cols = len(matrix[0])
n = len(matrix)

for i in range(0,rows):
    for j in range(0,cols):
        if i + j == n-1:
            print(matrix[i][j],end=" ")
## TC = O(n^2)

for i in range(0,rows):
    print(matrix[i][n-1-i],end=" ")
## TC = O(n)