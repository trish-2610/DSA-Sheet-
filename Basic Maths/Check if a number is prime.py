import math 

n = int(input("Enter Number : "))

if n <= 1:
    print("Not Prime")
else:
    is_prime = True

    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime")
    else:
        print("Not prime")

## TC = O(root(n))

## Interview Understanding
## If interviewer asks:
## “Why only till √n?”
## If a number has a big factor, then it must also have a small 
##  factor before √n. So checking after √n is useless.
