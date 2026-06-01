s1 = "abcd"
s2 = "cdab"

## Algorithm 
## s1 -> twice
## s1 = "abcdabcd"
## Outputs : "bcda","cdab","dabc"
## But length of both the strings should be same 

## Logic 
if len(s1) == len(s2) and s2 in (s1+s1):
    print("Rotation")
else:
    print("No Rotation")

## TC = O(n) String searching 
## SC = O(n) String concatenation (s1 + s1) = stores 2n characters

## A string is a rotation of another if it appears as a substring in the original string concatenated with itself, 
## provided both strings have the same length.