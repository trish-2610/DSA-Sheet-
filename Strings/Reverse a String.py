## Approach-1 (using indexing)
s = "Hello"
rev = s[::-1]
print(rev)

## TC = O(n) -> String has length n (traversal happens once)
## SC = O(n) -> A new reverse string is created of same length n

## Approach-2 (using a for loop)
rev_str = ""
for i in range(len(s)-1,-1,-1):
    rev_str += s[i]
print(rev_str)

## TC = O(n) -> Loop runs n times
## SC = O(n) -> A new rev_str is created of length n 