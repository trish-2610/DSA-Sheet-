n = int(input("Enter number : "))

# for i in range(1,n+1):
#     if n % i == 0:
#         print(i)
    
## TC = O(n)

import math
for i in range(1,int(math.sqrt(n))+1):
    if n % i == 0:
        print(i)
## more optimized version 
## But duplicates may come for perfect squares.(36,49,...)
