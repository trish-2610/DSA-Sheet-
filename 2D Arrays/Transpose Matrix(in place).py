matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

## square matrix , rows = cols 
n = len(matrix)

for i in range(0,n):
    for j in range(i+1,n):
        ## swap
        matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
print(matrix)

## logic (i==j) : No change
## i != j : Swap