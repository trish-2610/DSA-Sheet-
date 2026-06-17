# *********
#  *******
#   *****
#    ***
#     *

## just use reverse i (outer) loop

n = 5
for i in range(n-1,-1,-1): ## reverse loop
    ## spaces 
    for j in range(0,n-i-1):
        print(" ",end="")
    ## stars
    for j in range(0,2*i+1):
        print("*",end="")
    print()