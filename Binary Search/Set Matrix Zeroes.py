# Problem

# If any element in the matrix is 0,
# -> set its entire row and column to 0

## Hint : mark zeros then update

matrix = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,1,1]
]
rows = len(matrix)
cols = len(matrix[0])

## zeros count 
zero_rows = set() ## store 0 rows index number
zero_cols = set() ## store 0 columns index number

## Step - 1 : Find zeros and store the index number
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            zero_rows.add(i)
            zero_cols.add(j)

print(f"Zero rows index : {zero_rows} \nZero columns index : {zero_cols}")

## Update zeros
for i in range(rows):
    for j in range(cols):
        if i in zero_rows or j in zero_cols: ## either row or column , we have to update
            matrix[i][j] = 0 ## update zeros

## print matrix 
for row in matrix:
    print(row)

## Complexity
## TC = O(n × m)
## SC = O(n + m)