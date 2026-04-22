## Find the row index (or row number) which has the maximum sum
from pyparsing import matchPreviousExpr


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [2, 1, 2]
]

rows = len(matrix)
cols = len(matrix[0])
max_sum = float("-inf")
max_index = -1

for i in range(0,rows):
    row_sum = 0
    for j in range(0,cols):
        row_sum += matrix[i][j]

    if row_sum > max_sum:
        max_sum = row_sum
        max_index = i

print("Max sum = ",max_sum)
print("Max Index = ",max_index)
