## Iterative approach 
a = int(input("Enter a : "))
b = int(input("Enter b : "))

# while b != 0:
#     a , b = b , a% b 
# print(f"GCD is = {a}")

## Recursive approach
def gcd(a,b):
    
    if b == 0:
        return a 
    return gcd(b,a%b)
print(gcd(a,b))

## TC = O(log(min(a,b))) for both 
## Because numbers reduce quickly after each step.

# Space Complexity
# Iterative
# O(1)
# No extra space.

# Recursive
# O(log(min(a,b)))
# because of recursion stack.

# Why does Euclidean Algorithm work?
# Because the common divisors of a and b are the same as
# the common divisors of b and a % b.
