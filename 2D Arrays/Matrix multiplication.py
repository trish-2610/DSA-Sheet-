matrix1 = [
    [1,2,3],
    [1,3,4]
]
## shape 
m = len(matrix1) ## no. of rows
n = len(matrix1[0]) ## no. of cols

matrix2 = [
    [1,2,3,1],
    [4,3,2,2],
    [1,2,3,2]
]
p = len(matrix2) ## no. of rows
q = len(matrix2[0]) ## no. of cols

print(f"Matrix 1 : \n No. of rows = {m} and No. of cols = {n}\n Size = {m,n}")
print(f"Matrix 2 : \n No. of rows = {p} and No. of cols = {q}\n Size = {p,q}")

## matrix multiplication is possible when n == p
## means no. of cols in matrix1 should be equal to no. of rows in matrix2

## Output matrix size = m x q 

result_matrix = [
    [0,0,0,0],
    [0,0,0,0]
] ## size = 2 x 4 (m x q)

if n == p: ## matrix multiplication possible
    for i in range(0,m):
        for j in range(0,q):
            for k in range(0,p): ## either n or p (same value)
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    ## print matrix
    for row in result_matrix:
        print(row)
