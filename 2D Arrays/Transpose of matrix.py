# Transpose of Matrix
# Problem : Convert rows into columns.

# That means:
# matrix[i][j] → matrix[j][i]

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# rows = len(matrix)
# cols = len(matrix[0])

# for i in range(0,rows):
#     for j in range(0,cols):
#         print(matrix[j][i],end=" ")
#     print()

## But the above approach only works for square matrix
## TC = O(n x m)
## SC = O(1)

## General approach (for any matrix)   
# Program to transpose a matrix using a nested loop

matrix = [     
    [1, 2, 3],
    [4, 5, 6]
]
rows = len(matrix)
cols = len(matrix[0])

## create a resultant matrix with opposite dimensions of original 
## here 2 X 3 ----> 3 X 2 
result = [
    [0,0],
    [0,0],
    [0,0]
]

for i in range(rows):
    for j in range(cols):
        result[j][i] = matrix[i][j]
print(result)


## another way using list comprehension 
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
]
## it is 2 X 5 ----> 5 X 2 
## means i should run 5 times and j should run 2 times only (opposite of actual)
rows = len(matrix) ## 2
cols = len(matrix[0]) ## 5

transpose = [[matrix[j][i]
            for j in range(rows)] ## this inner loop will run 2 times
            for i in range(cols)] ## this outer loop will run 5 times
print(transpose)

## same thing without using list comprehension 
transpose = []
for i in range(cols):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)
print(transpose)

## Transpose (in place) -> square matrix
n = len(matrix)
for i in range(0,n):
    for j in range(i+1,n):
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]