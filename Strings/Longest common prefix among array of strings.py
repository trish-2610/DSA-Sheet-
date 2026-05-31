lst = ["car","cab","cat"]
lst.sort() ## firstly , sort the list 

## Now compare only first and last words in lst
first = lst[0]
last = lst[-1]
result = ""

for i in range(0,len(first)): ## for i in range( min(len(first),len(last)) )
    if first[i] == last[i]:
        result += first[i]
    else:
        break

print(result)

## TC =
## sorting = O(n log n)
## and compare at most m chars so O(m)
## Total TC = O(n log n + m)
## SC = O(1) Ignoring Python's internal sorting memory.