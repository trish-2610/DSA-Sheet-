#     *
#    ***
#   *****
#  *******
# *********  

## follow spaces and stars (print spaces then stars)
## spaces = n - i - 1
## Ex. if n = 3,
## i = 0 , spaces = 2
## i = 1 , spaces = 1
## i = 0 , spaces = 0

## stars = 2 * i + 1
## i = 0 , stars = 1
## i = 1 , stars = 3
## i = 2 , stars = 5

n = 5
for i in range(0,n):
    ## spaces 
    for j in range(0,n-i-1):
        print(" ",end="")
    ## stars 
    for j in range(0,2*i+1):
        print("*",end="")
    print()