from collections import Counter
s1 = "listen"
s2 = "silent"
is_anagram = Counter(s1) == Counter(s2)
print("Anagram" if is_anagram else "Not Anagram")
## TC = O(n) Counter traverse over string once
## SC = O(n) Counter stores frequency (worst case)

## using sorted
is_anagram = sorted(s1) == sorted(s2)
print("Anagram" if is_anagram else "Not Anagram")
0
## TC = O(n log n) ## sorting complexity O(n log n)
## SC = O(n) stores entire string 

## Counter is more optimized
## Using Counter gives O(n) time complexity because 
## it counts frequencies directly instead of sorting