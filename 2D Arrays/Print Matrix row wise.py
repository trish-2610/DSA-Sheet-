matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

# for row in matrix:
#     for element in row:
#         print(element,end=" ")
#     print()

## another way 
rows = len(matrix)
cols = len(matrix[0])

for i in range(0,rows): ## row-wise (as row is fixed)
    for j in range(0,cols): ## column-wise
        print(matrix[i][j],end=" ")
    print()

## Time complexity = O(n^2)