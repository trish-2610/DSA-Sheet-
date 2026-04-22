matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = 6
found = False
rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == target:
            print(f"Element found at Index : {i,j}")
            found = True
            break
if not found:
    print("Element not found") 