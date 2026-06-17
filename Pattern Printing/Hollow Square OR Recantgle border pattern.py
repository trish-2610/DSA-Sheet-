## Hollow square
n = 5
## *****
## *   *
## *   *
## *   *
## *****

## print stars when i = 0 , i = n-1 OR j = 0 , j = n-1 , otherwise print spaces
## Logic :
# i == 0 → top row
# i == n-1 → bottom row
# j == 0 → left column
# j == n-1 → right column

## This same boundary-condition trick is used in:
# Hollow Square
# Hollow Rectangle
# Hollow Pyramid
# Hollow Diamond
# Hollow Rhombus

for i in range(0,n):
    for j in range(0,n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

## Rectangular border pattern
rows = 5
cols = 4
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows-1 or j == 0 or j == cols-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()