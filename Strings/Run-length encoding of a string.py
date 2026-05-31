## Input : "aaabbc"
## Output : "a3b2c1"

s = "aaabbcaa"

count = 1 ## as we are starting from 1st index

for i in range(1,len(s)):
    if s[i] == s[i-1]: ## compare current with previous 
        count += 1 
    else: ## if not matched
        print(str(s[i-1])+str(count),end="")
        count = 1 ## again initializes with 1 
print(str(s[-1])+str(count)) ## prints last element with its count 

## TC = O(n) ## iterate only once over the string
## SC = O(1) ## No extra space used (only count variable)