# Zig-Zag Traversal (Row-wise)

# Problem
# Print matrix such that:

# Row 0 → left to right
# Row 1 → right to left
# Row 2 → left to right
# Row 3 → right to left

# Alternate direction for each row

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

for i in range(0,rows): ## traverse each row
    if i % 2 == 0: ## if row is even (normal order)
        for j in range(0,cols):
            print(matrix[i][j],end=" ")
    else: ## if row is odd (reverse order)
        for j in range(cols-1,-1,-1):
            print(matrix[i][j],end=" ")
    print()

# Time Complexity : O(n × m)
# (you traverse every element exactly once)

# Space Complexity : O(1)
# (no extra space used)