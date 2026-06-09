matrix = [
    [1 ,2 ,3],
    [4 ,5 ,6],
]

rows = len(matrix)
cols = len(matrix[0])

## 2 X 3 -> 3 X 2
transpose = []
for i in range(cols):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    transpose.append(row)
print(transpose)