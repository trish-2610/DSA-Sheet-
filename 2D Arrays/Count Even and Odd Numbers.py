matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

## variables
rows = len(matrix)
cols = len(matrix[0])
even_count = 0
odd_count = 0

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
print("Even count = ",even_count)
print("Odd count = ",odd_count)

## TC = O(n x m) or O(n^2)
## SC = O(1)