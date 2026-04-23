# Wave Traversal (Column-wise)
# Now we flip thinking:

# Instead of rows → we move column-wise

# Problem
# Column 0 → top to bottom
# Column 1 → bottom to top
# Column 2 → top to bottom

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

for j in range(0,cols): ## traversing column wise (j is fixed)
    if j % 2 == 0: ## if column(j) is even
        for i in range(0,rows): ## top to bottom (normal)
            print(matrix[i][j],end=" ")
    else: ## if column(j) is odd
        for i in range(rows-1,-1,-1): ## bottom to top (reverse)
            print(matrix[i][j],end=" ")
    print()

# Time Complexity : O(n × m)
# (you traverse every element exactly once)

# Space Complexity : O(1)
# (no extra space used)