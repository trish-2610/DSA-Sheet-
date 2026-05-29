sen = "Python is good"
words = sen.split()
rev_lst = []
for i in range(len(words)-1,-1,-1):
    rev_lst.append(words[i])
result = " ".join(rev_lst)
print(result)

## TC = O(n)
## SC = O(n) (words and rev_lst , extra list is created)

## more concise approach 
result = " ".join(sen.split()[::-1])
print(result)