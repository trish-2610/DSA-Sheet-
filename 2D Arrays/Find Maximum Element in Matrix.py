matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

max_element = float("-inf")
rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] > max_element:
            max_element = matrix[i][j]
print(max_element)

## TC = O(n x m) or O(n^2)
## SC = O(1)