n = 5
## Printing Pyramid (Inverted) (Upper Pyramid)
for i in range(n-1,-1,-1):
    ## spaces 
    for j in range(0,n-i-1):
        print(" ",end="")
    ## stars 
    for j in range(0,2*i+1):
        print("*",end="")
    print()
## Straight (Lower Pyramid)
for i in range(1,n): ## starting from 1st index to eliminate repeated row
    ## spaces 
    for j in range(0,n-i-1):
        print(" ",end="")
    ## stars
    for j in range(0,2*i+1):
        print("*",end="")
    print()