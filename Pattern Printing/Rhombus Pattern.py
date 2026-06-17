#     *****
#    *****
#   *****
#  *****
# *****

## Concept : Spaces and Stars
## at i = 0 , _ _ _ _ * * * * *
## at i = 1 , _ _ _ * * * * *
## at i = 2 , _ _ * * * * *
## at i = 3 , _ * * * * *
## at i = 4 , * * * * *

## spaces = n - i - 1
## stars = fixed (n)

n = 5
for i in range(0,n):
    ## spaces
    for j in range(0,n-i-1):
        print(" ",end="")
    ## stars
    print(n * "*")
    
## OR
for i in range(0,n):
    ## spaces
    for j in range(0,n-i-1):
        print(" ",end="")
    ## stars
    for j in range(0,n):
        print("*",end="")
    print()
    