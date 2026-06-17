#     *
#    ***
#   *****
#  *******
#   *****
#    ***
#     *

n = 4 
## Printing Pyramid (Normal) (Upper Pyramid)
for i in range(0,n):
    ## spaces 
    for j in range(0,n-i-1):
        print(" ",end="")
    ## stars 
    for j in range(0,2*i+1):
        print("*",end="")
    print()
## Printing Inverted Pyramid (Reverse) (Lower Pyramid)
for i in range(n-2,-1,-1): ## n-2 because 1 row is less
    ## spaces 
    for j in range(0,n-i-1):
        print(" ",end="")
    ## stars
    for j in range(0,2*i+1):
        print("*",end="")
    print()