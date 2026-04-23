## Rotate a square matrix (n × n) by 180 degrees clockwise
## Every element goes to completely opposite position
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

## Reverse each row in the matrix
for row in matrix:
    row.reverse()

## Reverse the row order 
## row order -> 0  1  2  make it to  ->  2  1  0
matrix.reverse()

## print
for row in matrix:
    print(row)