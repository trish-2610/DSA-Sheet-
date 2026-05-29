from operator import is_

from networkx import is_planar


s = "abba"
is_palindrome = s == s[::-1]
print("Palindrome" if is_palindrome else "Not Palindrome")

# Time Complexity
# Reversing string takes:
# O(n)
# Comparison also takes:
# O(n)
# Overall:
# O(n)
# Space Complexity
# Reversed string gets created.
# O(n)

## Optimized approach using Two pointers
left = 0
right = len(s) - 1
is_palindrome = True
while left < right:
    if s[left] != s[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
print("Palindrome" if is_palindrome else "Not Palindrome")
## TC = O(n)
## SC = O(1) ## NO extra string is used (in place)