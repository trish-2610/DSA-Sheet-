s = "madam"
result = ""
for char in s:
    if char not in result:
        result += char
print(result)
## TC = O(n^2) ## you are searching in whole result each time 
## SC = O(n)

## using set TC reduced to O(n) ## optimized and faster
seen = set()
result = ""
for char in s:
    if char not in seen:
        seen.add(char)
        result += char
print(result)