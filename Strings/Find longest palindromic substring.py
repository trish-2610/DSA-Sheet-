s = "aba"
longest = ""

for i in range(0,len(s)):
    for j in range(i,len(s)):
        sub = s[i:j+1] ## firstly find all possible substrings

        ## check whether the substring is palindrome
        if sub == sub[::-1]:
            
            ## check longest 
            if len(sub) > len(longest):
                longest = sub
print(longest)

## TC = O(n^3) 
## 2 loops = O(n^2) and palindrome check O(n)
## O(n^2 X n) -> O(n^3)
## SC = O(1) 