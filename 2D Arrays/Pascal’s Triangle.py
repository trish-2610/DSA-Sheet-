# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

## logic :
## current = above + above left 
## current[i][j] = previous[i-1][j] + previous[i-1][j-1]

n = 5
triangle = []

for i in range(0,n):
    row = [1] * (i+1) ## create rows of 1s one by one  ------
                                                            #
    ## key part of the program                              #
    ## we have to update the rows                           # Write these 2 steps first
    for j in range(1,i):                                    #
        row[j] = triangle[i-1][j] + triangle[i-1][j-1]      #
                                                            #
    triangle.append(row)                              #------
 
for row in triangle:
    print(row)